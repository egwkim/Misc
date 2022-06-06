from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler
from io import BytesIO
from multiprocessing import Process, Queue
import socket
import os
import json
import time


HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8080))
TIMEOUT = 10


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = BytesIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message


class NotFoundException(Exception):
    pass


class TimeoutException(Exception):
    pass


class InvalidRequestException(Exception):
    pass


def factor(n: int, q: Queue = None):
    if n < 2:
        return
    factors = []
    k = 2
    while n != 1:
        if n % k == 0:
            n //= k
            factors.append(k)
        else:
            k += 1
    if q != None:
        q.put(factors)
        return
    return factors


def handleConnection(conn, addr):
    res = ""
    try:
        # Parse request
        recv = conn.recv(4096)
        print(recv)
        req = HTTPRequest(recv)
        if req.error_code != None:
            res = f"HTTP/1.0 {req.error_code} {req.error_message}\n\n"
            raise InvalidRequestException(
                f"{req.error_code} {req.error_message}")
        try:
            parsed = urlparse(req.path)
        except AttributeError:
            return
        path = parsed.path
        query = parse_qs(parsed.query)
        host = req.headers.get("Host")
        res = ''
        if not path == "/":
            raise NotFoundException("Path not found")
        if not query:
            res = f"HTTP/1.0 200 OK\n\nPrime Factorization\nQuery with n=number\nn must be an intege and bigger than one\nExample {host}/?n=10\n"
            return
        try:
            n_list = query['n']
        except KeyError:
            raise NotFoundException("Invalid query")

        # Process request
        factor_list = {}
        for n in n_list:
            try:
                n = int(n)
                if n <= 1:
                    continue
                q = Queue()
                p = Process(target=factor, args=(n, q))
                p.start()
                p.join(TIMEOUT)
                if p.is_alive():
                    p.terminate()
                    p.join()
                if q.empty():
                    raise TimeoutException("Timeout while prime factorizing")
                factor_list[str(n)] = q.get()
            except ValueError:
                continue
        if factor_list:
            res = "HTTP/1.0 200 OK\n\n" + json.dumps(factor_list) + "\n"
        else:
            raise NotFoundException("Invalid query")

    # Handle exceptions and send response
    except InvalidRequestException as e:
        print(e)
    except NotFoundException as e:
        res = f"HTTP/1.0 404 Not Found\n\n{e}\n"
    except TimeoutException as e:
        res = f"HTTP/1.0 503 Service Unavailable\n\n{e}\n"
    finally:
        conn.sendall(res.encode())


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"{PORT = }")
        while True:
            conn, addr = s.accept()
            with conn:
                p = Process(target=handleConnection, args=(conn, addr))
                p.daemon = False
                p.start()


if __name__ == "__main__":
    main()
