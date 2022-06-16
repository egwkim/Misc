from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler
from io import BytesIO
from multiprocessing import Process
import socket
import os
import json


HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8080))
TIMEOUT = 10
PROTOCOL = "HTTP/1.0"


class HTTPResponse():
    def __init__(self, code, body="", protocol=PROTOCOL):
        self.code = code
        self.body = body
        self.protocol = protocol

    def __str__(self):
        return f"{self.protocol} {self.code}\n\n{self.body}"

    def encode(self):
        return self.__str__().encode()


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = BytesIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message


class HTTPError(Exception):
    def __init__(self, code: str, message: str = None):
        super().__init__(message)
        self.code = code
        if message == None:
            self.message = self.code + "\n"
        else:
            self.message = message

    def __str__(self):
        return self.message

    def http_response(self):
        return HTTPResponse(self.code, self.message)


def factor(n: int):
    if n < 2:
        return

    factors = []

    # Check 2
    k = 2
    while n % k == 0:
        n //= k
        factors.append(k)

    # Check odd numbers until k * k < n
    k = 3
    while k * k < n:
        if n % k == 0:
            n //= k
            factors.append(k)
        else:
            k += 2

    # If n > 1, n is a prime number
    if n > 1:
        factors.append(n)

    return factors


def processConnection(conn, addr):
    with conn:
        res = ""
        try:
            # Parse request
            recv = conn.recv(4096)
            req = HTTPRequest(recv)
            if req.error_code != None:
                raise HTTPError(f"{req.error_code} {req.error_message}")
            try:
                parsed = urlparse(req.path)
            except AttributeError:
                return
            path = parsed.path
            query = parse_qs(parsed.query)
            host = req.headers.get("Host")
            res = ''
            if not path == "/":
                raise HTTPError("404 Not Found", "Path not found\n")
            if not query:
                res = HTTPResponse(
                    "200 OK", f"Prime Factorization\nQuery with n=number\nn must be an intege and bigger than one\nExample {host}/?n=10\n")
                return
            try:
                n_list = query['n']
            except KeyError:
                raise HTTPError("404 Not Found", "Invalid query\n")

            # Process request
            factor_list = {}
            for n in n_list:
                try:
                    n = int(n)
                    if n <= 1:
                        continue
                    factor_list[str(n)] = factor(n)
                except ValueError:
                    continue
            if factor_list:
                res = "HTTP/1.0 200 OK\n\n" + json.dumps(factor_list) + "\n"
            else:
                raise HTTPError("404 Not Found", "Invalid query\n")

        # Handle exceptions and send response
        except HTTPError as e:
            print(e)
            res = e.http_response()
        finally:
            if res == "":
                res = HTTPResponse("500 Internal Server Error")
            conn.sendall(res.encode())


def handleConnection(conn, addr):
    try:
        p = Process(target=processConnection, args=(conn, addr))
        p.start()
        p.join(TIMEOUT)
        if p.is_alive():
            p.terminate()
            p.join()
            raise HTTPError("503 Service Unavailable",
                            "Timeout while processing the request\n")
    except HTTPError as e:
        res = e.http_response()
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
                p.start()


if __name__ == "__main__":
    main()
