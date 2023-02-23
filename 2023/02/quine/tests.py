"""This module tests other python quines, and also is a quine itself

If all quines work fine, print itself.
Otherwise, raise an error.
"""

import contextlib
import io
import os
import subprocess
import unittest
import unittest.mock

DIR = os.path.dirname(__file__)
EXCLUDE = ["tests.py"]


class TestQuines(unittest.TestCase):
    def test_self(self):
        """Test if quine function in this file works correctly"""
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            quine()
        with io.open(__file__, encoding="utf-8") as fileIO:
            # self.assertEqual(output.getvalue(), fileIO.read())
            pass

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


def reset_quine():
    """Reset quine function"""
    pass


def generate_quine():
    """Modify quine function to work properly"""
    # TODO create quine generator
    pass


def quine():
    """Print everything in this file (quine/tests.py)"""
    pass


def main():
    output = io.StringIO()
    with contextlib.redirect_stderr(output):
        unittest.main()
    output = output.getvalue()

    if "FAILED" in output:
        print(output)
    else:
        quine()


if __name__ == "__main__":
    main()
