"""
A test code for FFT.py
"""

import FFT
import unittest


class TestFFT(unittest.TestCase):

    def test_inverse(self):
        P_list = [
            [1, 2, 3, 4],
            [2, 6],
            [9, -32, 349, -1],
            [32, 55, 1, 3],
            [1, 2, 3, 4, 5, -6, -7, 8],
            [1+2j, 3+4j, 5+6j, 7+8j]
        ]

        for P in P_list:
            P_1 = FFT.IFFT(FFT.FFT(P))
            P_2 = FFT.FFT(FFT.IFFT(P))
            error_1 = sum(P_1) - sum(P)
            error_2 = sum(P_2) - sum(P)
            self.assertAlmostEqual(error_1, 0)
            self.assertAlmostEqual(error_2, 0)


if __name__ == "__main__":
    unittest.main()
