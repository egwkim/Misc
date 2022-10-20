import math


def calc_primes(n: int) -> list[bool]:
    """
    Calculate prime numbers up to n

    Returns:
        list[bool]: list[i] shows if i is a prime number.
    """
    p = [True] * (n + 1)
    p[0] = False
    p[1] = False

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if p[i]:
            for j in range(i*i, n+1, i):
                p[j] = False
    return p


def main():
    # Input an even number
    n = int(input())
    if not n > 0:
        return
    if n % 2:
        return

    # Calculate prime numbers
    primes = calc_primes(n)

    # Brute force
    for i, p in enumerate(primes):
        if p and primes[n - i]:
            print(i, n-i)
            return


if __name__ == '__main__':
    main()
