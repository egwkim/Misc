"""This module tests other python quines, and also is a quine itself

If all quines work fine, print itself.
Otherwise, raise an error.
"""

import os

DIR = os.path.dirname(__file__)


def test_self():
    """Test if quine function in this file works correctly"""
    # TODO test itself
    pass


def test_single_quine(filepath: str):
    """Test given quine"""
    

def test_other_python_quines():
    """Test all quines excluding this file"""
    files = [f for f in os.listdir(DIR)]

    for f in files:
        if not os.path.isfile(os.path.join(DIR, f)):
            continue
        if "python" in f or f.split(".")[-1] == "py":
            # TODO Test python code
            pass


def generate_quine():
    """Modify quine function to work properly"""
    # TODO create quine generator
    pass


def quine():
    """Print everything in this file (quine/tests.py)"""
    pass


def main():
    test_other_python_quines()
    test_self()
    quine()


if __name__ == "__main__":
    main()
