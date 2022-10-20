import math
import matplotlib.pyplot as plt


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


def goldbach_pair(n: int) -> tuple[int, int]:
    if not n > 3 or n % 2:
        raise ValueError

    # Calculate prime numbers
    primes = calc_primes(n)

    # Brute force
    for i, p in enumerate(primes):
        if p and primes[n - i]:
            return (i, n-i)


def visualize(n: int):
    if not n > 3:
        raise ValueError
    primes = calc_primes(n)

    x = []
    y = []
    cnt = [0] * (n+1)
    cnt_graph_max = 0

    for k in range(4, n + 1, 2):
        for i, p in enumerate(primes):
            if p and primes[k - i]:
                x.append(i)
                y.append(k-i)
                cnt[i] += 1
                cnt_graph_max = max(cnt_graph_max, i)
                break

    if not (n > 10**7):
        plt.plot(x, y, '.')
        plt.show()

    plt.yscale('log')
    plt.plot(range(cnt_graph_max+1), cnt[:cnt_graph_max+1], '.')
    plt.show()


def main():
    """# Calculate Goldbach pair
    # Input an even number
    n = int(input())
    print(goldbach_pair(n))
    """

    visualize(int(input()))


if __name__ == '__main__':
    main()
