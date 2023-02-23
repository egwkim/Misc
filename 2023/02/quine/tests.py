import os

desc = """
This file tests other python quines, and also is a quine itself!
If all quines work fine, print itself.
Otherwise, raise an error.
"""

DIR = os.path.dirname(__file__)


def generate_quine():
    """
    Modifies quine function to work properly.
    """


def quine():
    """
    Print everything in this file.
    """
    # TODO print itself
    pass


def test_self():
    """
    Test if quine() in this file works correctly.
    """
    # TODO test itself
    pass


def test_other_python_quines():
    """
    Test all quines without this file.
    """
    files = [f for f in os.listdir(DIR)]

    for f in files:
        if not os.path.isfile(os.path.join(DIR, f)):
            continue
        if "python" in f or f.split(".")[-1] == "py":
            # TODO Test python code
            pass


def main():
    test_other_python_quines()
    test_self()
    quine()


if __name__ == "__main__":
    main()
