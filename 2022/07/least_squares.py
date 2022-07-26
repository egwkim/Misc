"""
Get the linear function that best fits the given data.
"""

from collections.abc import Sequence
from typing import Tuple


def least_squares(x_list: Sequence[float], y_list: Sequence[float]) -> Tuple[float, float]:
    """
    Get the linear function that best fits the given data.
    y = ax + b
    Returns (a, b)
    """
    n = len(x_list)
    if len(y_list) != n:
        raise ValueError('Lengths of x_list and y_list do not match.')
    x = sum(x_list)
    xx = sum(x*x for x in x_list)
    y = sum(y_list)
    # yy = sum(y*y for y in y_list)
    xy = sum(x*y for x, y in zip(x_list, y_list))
    a = (xy - x*y/n) / (xx - x*x/n)
    b = (y - a*x) / n
    return (a, b)


if __name__ == '__main__':
    x_list = range(10)
    y_list = range(0, 20, 2)
    print(least_squares(x_list, y_list))
