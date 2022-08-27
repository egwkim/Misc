def pisano_period(n: int):
    i = 0
    a = 0
    b = 1
    while 1:
        i += 1
        t = b
        b = (a+b) % n
        a = t % n
        if a == 0 and b == 1:
            break
        if a == 0 and b == n-1:
            i *= 2
            break
    return i


def main():
    print(pisano_period(int(input())))


if __name__ == '__main__':
    main()
