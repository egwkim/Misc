"""
Created after watching https://www.youtube.com/watch?v=h7apO7q16V0
"""

import cmath


def FFT(P):
    """
    Computes the value representation of the given polynomial.
    The degree of the given polynomial should be the power of two.

    Args:
        P (list): Coefficient representation of the polynomial

    Returns:
        list: Value representation of the given polynomial
    """
    n = len(P)
    half_n = int(n/2)

    if n == 1:
        return P

    w = [cmath.exp(2*cmath.pi*1j*i/n) for i in range(half_n)]

    P_e = []
    P_o = []
    for i in range(half_n):
        P_e.append(P[i*2])
        P_o.append(P[i*2+1])

    y = [0]*n

    y_e = FFT(P_e)
    y_o = FFT(P_o)

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
    half_n = int(n/2)

    if n == 1:
        return P

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
    P_coeff = [1, 2, 3, 4]
    P_value = FFT(P_coeff)

    print(P_value)
    print(IFFT(P_value))

    test_case = [
        [1, 2, 3, 4],
        [2, 6],
        [9, -32, 349, -1],
        [32, 55, 1, 3],
        [1, 2, 3, 4, 5, -6, -7, 8],
        [1+2j, 3+4j, 5+6j, 7+8j]
    ]

    for i, x in enumerate(test_case):
        # Calculate the IFFT of the FFT and compare it to the original P to check for errors.
        y = IFFT(FFT(x))
        # Error is calculated as the Sum of Squares of the Error (for each coefficients).
        print(f"Test case no {i}, Error: {sum((j-k)**2 for j,k in zip(x,y))}")
