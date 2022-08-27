from typing import List


def continued_fraction(a: List[float]):
    result = 0
    for _ in range(len(a) - 1):
        result += a.pop()
        result = 1/result
    result += a.pop()
    return result


def main():
    # Continued fraction of geometric progression
    for i in range(11, 51):
        print(i/10, continued_fraction([(i/10)
              ** j for j in range(100)]), sep='\t')

    print()

    # Continued fraction of natural number
    print(continued_fraction([i for i in range(1, 100)]))


if __name__ == '__main__':
    main()
