"""
Created after watching https://www.youtube.com/watch?v=h7apO7q16V0
"""

# TODO Add polynomial multiplication example.


import math
import cmath


def nextpow2(n):
    return 2**math.ceil(math.log2(n))


def extend_list_with_zeroes(l, n):
    return l + [0] * (n-len(l))


def FFT(P, base=True):
    """
    Computes the value representation of the given polynomial.
    The degree of the given polynomial should be the power of two.
    If not, automatically extends the list by adding zeroes at the end.

    Args:
        P (list): Coefficient representation of the polynomial

    Returns:
        list: Value representation of the given polynomial
    """
    n = len(P)
    if n == 1:
        return P

    if base:
        original_n = n
        n = nextpow2(n)
        if n != original_n:
            P = extend_list_with_zeroes(P, n)
            print(P)

    half_n = int(n/2)

    w = [cmath.exp(2*cmath.pi*1j*i/n) for i in range(half_n)]

    P_e = []
    P_o = []
    for i in range(half_n):
        P_e.append(P[i*2])
        P_o.append(P[i*2+1])

    y = [0]*n

    y_e = FFT(P_e, False)
    y_o = FFT(P_o, False)

    for i in range(half_n):
        y[i] = y_e[i] + w[i]*y_o[i]
        y[i+half_n] = y_e[i] - w[i]*y_o[i]

    return y


def IFFT(P, base=True):
    """
    Computes the coefficient representation of the given polynomial with the value representation.
    The degree of the given polynomial should be the power of two.

    Args:
        P (list): Value representation of the polynomial

    Returns:
        list: Coefficient representation of the given polynomial
    """
    n = len(P)
    if n == 1:
        return P

    half_n = int(n/2)

    w = [cmath.exp(-2*cmath.pi*1j*i/n) for i in range(half_n)]

    P_e = []
    P_o = []
    for i in range(half_n):
        P_e.append(P[i*2])
        P_o.append(P[i*2+1])

    y = [0]*n

    y_e = IFFT(P_e, False)
    y_o = IFFT(P_o, False)

    for i in range(half_n):
        y[i] = y_e[i] + w[i]*y_o[i]
        y[i+half_n] = y_e[i] - w[i]*y_o[i]

    if not base:
        return y

    return [i/n for i in y]


if __name__ == "__main__":
    P_coeff = [1, 2, 3, 4, 5]
    P_value = FFT(P_coeff)

    print(P_value)
    print(IFFT(P_value))
