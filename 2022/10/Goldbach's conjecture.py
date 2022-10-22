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
    """
    Visualize small pairs
    """
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


def visualize2(n: int):
    """
    Visualize small pairs containing 3 or 5
    """
    primes = calc_primes(n-3)
    cnt_3 = 0
    cnt_5 = 0
    x_3 = []
    x_5 = []
    y_3 = []
    y_5 = []
    for i in range(6, n + 1, 2):
        if primes[i-3]:
            cnt_3 += 1
            x_3.append(i)
            y_3.append(cnt_3)
        elif primes[i-5]:
            cnt_5 += 1
            x_5.append(i)
            y_5.append(cnt_5)

    # Number of pairs
    plt.plot(x_3, y_3)
    plt.plot(x_5, y_5)
    plt.show()

    # Slope
    plt.plot(x_3[1:],
             list((i+1) / (x_3[i+1] - x_3[0]) for i in range(len(x_3)-1)))
    plt.plot(x_5[1:],
             list((i+1) / (x_5[i+1] - x_5[0]) for i in range(len(x_5)-1)))
    plt.show()


def visualize3(n: int):
    """
    Predict small pair distribution
    """
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
    plt.yscale('log')
    plt.plot(range(cnt_graph_max+1), cnt[:cnt_graph_max+1], '.')

    # Prediction
    # TODO Fix prediction
    # TODO Change graph range
    x = []
    y = []
    value_list = [1] * n
    for i, p in enumerate(primes):
        if p and i % 2:
            if i > n/2:
                break
            x.append(i)
            s = 0
            
            # Calculate integral numerically
            # Integral from i*2 to n (1-1/ln(x-3))(1-1/ln(x-5)) ... (1-1/ln(x-p))(1/ln(x-i)) dx
            # where p is the greatest prime smaller than i
            for j in range(i*2, n):
                l = 1 / math.log(j-i)
                s += value_list[j-i] * l
                value_list[j-i] *= (1 - l)
            y.append(s)
    plt.plot(x, y)
    plt.show()


def main():
    """# Calculate Goldbach pair
    # Input an even number
    n = int(input())
    print(goldbach_pair(n))
    """

    visualize2(int(input()))


if __name__ == '__main__':
    main()
