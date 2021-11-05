import unittest
from pairing_socks import *

# test input 1 (30 elements in array)
sock_pile1 = [3, 1, 3, 4, 7, 9, 6, 9, 2, 0, 3, 5, 1, 10, 6, 5, 7, 8, 3, 4, 8, 7, 9, 11, 1, 3, 9, 5, 4, 6]
pile1_len = len(sock_pile1)

# test input 2 (80 elements in array)
sock_pile2 = [10, 7, 8, 9, 7, 2, 52, 10, 8, 1, 5, 6, 7, 8, 9, 14, 15, 16, 13, 18, 17, 16, 23, 23, 45, 10, 12, 8, 7,
             5, 6, 4, 2, 1, 3, 17, 15, 12, 11, 13, 10, 12, 18, 10, 11, 1, 3, 4, 6, 7, 8, 9, 7, 7, 13, 8, 15, 12,
             10, 4, 4, 7, 14, 15, 13, 14, 20, 21, 45, 12, 14, 17, 21, 1, 20, 15, 21, 3, 4, 52]
pile2_len = len(sock_pile2)


class PairingSocksTest(unittest.TestCase):
    def test_sock_pairing(self):
        self.assertEqual(matchSock(sock_pile1, pile1_len), 10)
        self.assertEqual(matchSock(sock_pile2, pile2_len), 36)


if __name__ == '__main__':
    unittest.main()
