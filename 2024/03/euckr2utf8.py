# One liner
# python -c 'with open(<path>, encoding="euc-kr") as f: print(f.read())'


def euckr2utf8(filename):
    with open(filename, "r", encoding="euc-kr") as f:
        return f.read()


if __name__ == "__main__":
    import sys

    filename = ""
    if len(sys.argv) == 1:
        while filename != "":
            filename = input("Enter filename: ")
    else:
        filename = sys.argv[1]
    print(euckr2utf8(filename))
    print(type(filename))
