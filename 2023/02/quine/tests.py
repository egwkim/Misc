"""This module tests other python quines, and also is a quine itself

If all quines work fine, print itself.
Otherwise, raise an error.
"""

import base64
import contextlib
import io
import os
import shutil
import subprocess
import unittest

DIR = os.path.dirname(__file__)
EXCLUDE = ["tests.py"]


class TestQuines(unittest.TestCase):
    def test_self(self):
        """Test if quine function in this file works correctly"""
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            quine()
        with io.open(__file__, encoding="utf-8") as fileIO:
            self.assertEqual(output.getvalue(), fileIO.read())

    def test_other_python_quines(self):
        """Test all quines excluding this file"""
        files = [f for f in os.listdir(DIR)]

        for filename in files:
            filepath = os.path.join(DIR, filename)
            if not os.path.isfile(filepath):
                continue
            if filename in EXCLUDE:
                continue

            if "python" in filename or filename.split(".")[-1] == "py":
                with self.subTest(filepath=filepath):
                    with io.open(filepath, encoding="utf-8") as fileIO:
                        output = (
                            subprocess.check_output(["python", filepath])
                            .decode()
                            .replace("\r", "")
                        )
                        self.assertEqual(output, fileIO.read())


def backup():
    shutil.copy2(__file__, __file__ + ".back")


def encode(s: str):
    return base64.b64encode(s.encode())


def decode(s: str):
    return base64.b64decode(s).decode()


def reset_quine(do_backup=True):
    """Regenerate quine function"""
    if do_backup:
        backup()
    with io.open(__file__, mode="r+", encoding="utf-8") as file:
        head = ""
        while l := file.readline():
            head += l
            if l.startswith("def quine():"):
                break
        if not l:
            raise NotImplementedError()

        head += file.readline()  # Skip docstring
        offset = file.tell()  # Start of quine function
        file.seek(offset)

        # Search the end of the quine function
        while l := file.readline():
            if l.startswith("def"):
                break
        if not l:
            raise NotImplementedError()

        mid = ""

        tail = (
            "    print(decode(head), end='')\n"
            + '    print(f"    {head=}")\n'
            + '    print(f"    {tail=}")\n'
            + "    print(decode(tail), end='')\n"
            + "\n\n"
            + l
            + file.read()
        )  # Contents after the quine function

        file.seek(offset)
        file.truncate()
        file.writelines(
            [
                f"    {i}\n"
                for i in [
                    f"head={encode(head)}",
                    f"tail={encode(tail)}",
                ]
            ]
        )
        file.write(tail)


def quine():
    """Print everything in this file (quine/tests.py)"""
    head=b'IiIiVGhpcyBtb2R1bGUgdGVzdHMgb3RoZXIgcHl0aG9uIHF1aW5lcywgYW5kIGFsc28gaXMgYSBxdWluZSBpdHNlbGYKCklmIGFsbCBxdWluZXMgd29yayBmaW5lLCBwcmludCBpdHNlbGYuCk90aGVyd2lzZSwgcmFpc2UgYW4gZXJyb3IuCiIiIgoKaW1wb3J0IGJhc2U2NAppbXBvcnQgY29udGV4dGxpYgppbXBvcnQgaW8KaW1wb3J0IG9zCmltcG9ydCBzaHV0aWwKaW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IHVuaXR0ZXN0CgpESVIgPSBvcy5wYXRoLmRpcm5hbWUoX19maWxlX18pCkVYQ0xVREUgPSBbInRlc3RzLnB5Il0KCgpjbGFzcyBUZXN0UXVpbmVzKHVuaXR0ZXN0LlRlc3RDYXNlKToKICAgIGRlZiB0ZXN0X3NlbGYoc2VsZik6CiAgICAgICAgIiIiVGVzdCBpZiBxdWluZSBmdW5jdGlvbiBpbiB0aGlzIGZpbGUgd29ya3MgY29ycmVjdGx5IiIiCiAgICAgICAgb3V0cHV0ID0gaW8uU3RyaW5nSU8oKQogICAgICAgIHdpdGggY29udGV4dGxpYi5yZWRpcmVjdF9zdGRvdXQob3V0cHV0KToKICAgICAgICAgICAgcXVpbmUoKQogICAgICAgIHdpdGggaW8ub3BlbihfX2ZpbGVfXywgZW5jb2Rpbmc9InV0Zi04IikgYXMgZmlsZUlPOgogICAgICAgICAgICBzZWxmLmFzc2VydEVxdWFsKG91dHB1dC5nZXR2YWx1ZSgpLCBmaWxlSU8ucmVhZCgpKQoKICAgIGRlZiB0ZXN0X290aGVyX3B5dGhvbl9xdWluZXMoc2VsZik6CiAgICAgICAgIiIiVGVzdCBhbGwgcXVpbmVzIGV4Y2x1ZGluZyB0aGlzIGZpbGUiIiIKICAgICAgICBmaWxlcyA9IFtmIGZvciBmIGluIG9zLmxpc3RkaXIoRElSKV0KCiAgICAgICAgZm9yIGZpbGVuYW1lIGluIGZpbGVzOgogICAgICAgICAgICBmaWxlcGF0aCA9IG9zLnBhdGguam9pbihESVIsIGZpbGVuYW1lKQogICAgICAgICAgICBpZiBub3Qgb3MucGF0aC5pc2ZpbGUoZmlsZXBhdGgpOgogICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgaWYgZmlsZW5hbWUgaW4gRVhDTFVERToKICAgICAgICAgICAgICAgIGNvbnRpbnVlCgogICAgICAgICAgICBpZiAicHl0aG9uIiBpbiBmaWxlbmFtZSBvciBmaWxlbmFtZS5zcGxpdCgiLiIpWy0xXSA9PSAicHkiOgogICAgICAgICAgICAgICAgd2l0aCBzZWxmLnN1YlRlc3QoZmlsZXBhdGg9ZmlsZXBhdGgpOgogICAgICAgICAgICAgICAgICAgIHdpdGggaW8ub3BlbihmaWxlcGF0aCwgZW5jb2Rpbmc9InV0Zi04IikgYXMgZmlsZUlPOgogICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSAoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBzdWJwcm9jZXNzLmNoZWNrX291dHB1dChbInB5dGhvbiIsIGZpbGVwYXRoXSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIC5kZWNvZGUoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgLnJlcGxhY2UoIlxyIiwgIiIpCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICAgICAgc2VsZi5hc3NlcnRFcXVhbChvdXRwdXQsIGZpbGVJTy5yZWFkKCkpCgoKZGVmIGJhY2t1cCgpOgogICAgc2h1dGlsLmNvcHkyKF9fZmlsZV9fLCBfX2ZpbGVfXyArICIuYmFjayIpCgoKZGVmIGVuY29kZShzOiBzdHIpOgogICAgcmV0dXJuIGJhc2U2NC5iNjRlbmNvZGUocy5lbmNvZGUoKSkKCgpkZWYgZGVjb2RlKHM6IHN0cik6CiAgICByZXR1cm4gYmFzZTY0LmI2NGRlY29kZShzKS5kZWNvZGUoKQoKCmRlZiByZXNldF9xdWluZShkb19iYWNrdXA9VHJ1ZSk6CiAgICAiIiJSZWdlbmVyYXRlIHF1aW5lIGZ1bmN0aW9uIiIiCiAgICBpZiBkb19iYWNrdXA6CiAgICAgICAgYmFja3VwKCkKICAgIHdpdGggaW8ub3BlbihfX2ZpbGVfXywgbW9kZT0icisiLCBlbmNvZGluZz0idXRmLTgiKSBhcyBmaWxlOgogICAgICAgIGhlYWQgPSAiIgogICAgICAgIHdoaWxlIGwgOj0gZmlsZS5yZWFkbGluZSgpOgogICAgICAgICAgICBoZWFkICs9IGwKICAgICAgICAgICAgaWYgbC5zdGFydHN3aXRoKCJkZWYgcXVpbmUoKToiKToKICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgaWYgbm90IGw6CiAgICAgICAgICAgIHJhaXNlIE5vdEltcGxlbWVudGVkRXJyb3IoKQoKICAgICAgICBoZWFkICs9IGZpbGUucmVhZGxpbmUoKSAgIyBTa2lwIGRvY3N0cmluZwogICAgICAgIG9mZnNldCA9IGZpbGUudGVsbCgpICAjIFN0YXJ0IG9mIHF1aW5lIGZ1bmN0aW9uCiAgICAgICAgZmlsZS5zZWVrKG9mZnNldCkKCiAgICAgICAgIyBTZWFyY2ggdGhlIGVuZCBvZiB0aGUgcXVpbmUgZnVuY3Rpb24KICAgICAgICB3aGlsZSBsIDo9IGZpbGUucmVhZGxpbmUoKToKICAgICAgICAgICAgaWYgbC5zdGFydHN3aXRoKCJkZWYiKToKICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgaWYgbm90IGw6CiAgICAgICAgICAgIHJhaXNlIE5vdEltcGxlbWVudGVkRXJyb3IoKQoKICAgICAgICBtaWQgPSAiIgoKICAgICAgICB0YWlsID0gKAogICAgICAgICAgICAiICAgIHByaW50KGRlY29kZShoZWFkKSwgZW5kPScnKVxuIgogICAgICAgICAgICArICcgICAgcHJpbnQoZiIgICAge2hlYWQ9fSIpXG4nCiAgICAgICAgICAgICsgJyAgICBwcmludChmIiAgICB7dGFpbD19IilcbicKICAgICAgICAgICAgKyAiICAgIHByaW50KGRlY29kZSh0YWlsKSwgZW5kPScnKVxuIgogICAgICAgICAgICArICJcblxuIgogICAgICAgICAgICArIGwKICAgICAgICAgICAgKyBmaWxlLnJlYWQoKQogICAgICAgICkgICMgQ29udGVudHMgYWZ0ZXIgdGhlIHF1aW5lIGZ1bmN0aW9uCgogICAgICAgIGZpbGUuc2VlayhvZmZzZXQpCiAgICAgICAgZmlsZS50cnVuY2F0ZSgpCiAgICAgICAgZmlsZS53cml0ZWxpbmVzKAogICAgICAgICAgICBbCiAgICAgICAgICAgICAgICBmIiAgICB7aX1cbiIKICAgICAgICAgICAgICAgIGZvciBpIGluIFsKICAgICAgICAgICAgICAgICAgICBmImhlYWQ9e2VuY29kZShoZWFkKX0iLAogICAgICAgICAgICAgICAgICAgIGYidGFpbD17ZW5jb2RlKHRhaWwpfSIsCiAgICAgICAgICAgICAgICBdCiAgICAgICAgICAgIF0KICAgICAgICApCiAgICAgICAgZmlsZS53cml0ZSh0YWlsKQoKCmRlZiBxdWluZSgpOgogICAgIiIiUHJpbnQgZXZlcnl0aGluZyBpbiB0aGlzIGZpbGUgKHF1aW5lL3Rlc3RzLnB5KSIiIgo='
    tail=b'ICAgIHByaW50KGRlY29kZShoZWFkKSwgZW5kPScnKQogICAgcHJpbnQoZiIgICAge2hlYWQ9fSIpCiAgICBwcmludChmIiAgICB7dGFpbD19IikKICAgIHByaW50KGRlY29kZSh0YWlsKSwgZW5kPScnKQoKCmRlZiBtYWluKCk6CiAgICBvdXRwdXQgPSBpby5TdHJpbmdJTygpCiAgICB3aXRoIGNvbnRleHRsaWIucmVkaXJlY3Rfc3RkZXJyKG91dHB1dCk6CiAgICAgICAgdW5pdHRlc3QubWFpbihleGl0PUZhbHNlKQogICAgb3V0cHV0ID0gb3V0cHV0LmdldHZhbHVlKCkKCiAgICBpZiAiRkFJTEVEIiBpbiBvdXRwdXQ6CiAgICAgICAgcHJpbnQob3V0cHV0KQogICAgZWxzZToKICAgICAgICBxdWluZSgpCiAgICByZXNldF9xdWluZSgpCgoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo='
    print(decode(head), end='')
    print(f"    {head=}")
    print(f"    {tail=}")
    print(decode(tail), end='')


def main():
    output = io.StringIO()
    with contextlib.redirect_stderr(output):
        unittest.main(exit=False)
    output = output.getvalue()

    if "FAILED" in output:
        print(output)
    else:
        quine()
    reset_quine()


if __name__ == "__main__":
    main()
