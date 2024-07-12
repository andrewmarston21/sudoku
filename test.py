import unittest

from csvs import read_csv
from main import print_board
from backtrack import _get_neighbors, _is_consistent

class TestCSVImport(unittest.TestCase):
    def test_read_csv(self):
        o = [1,2,3,4,5,6,7,8,9]
        expected_board = [o,o,o, [4],o,[1], o,o,[3], [2],[5],o, o,o,[7], o,o,o, o,[9],o, o,o,o, [8],[5],o, \
                          o,o,[4], [2],o,o, o,o,o, [1],o,o, o,o,o, o,o,[6], o,o,[6], o,o,o, [7],o,o, \
                          [8],o,o, o,[1],o, [5],o,o, [9],o,o, [5],o,o, o,o,o, o,o,o, o,[9],o, o,[3],[1]]
        actual_board = read_csv("csvs/board_24873.csv")
        print("Board generated by csvs.read_csv('csvs/board_24873.csv'): ")
        print_board(actual_board)
        self.assertEqual(actual_board, expected_board)

    def test__get_neighbors(self):
        square = 1
        print("Testing square=1")
        expected_neighbors = {0,1,2,3,4,5,6,7,8,9,10,11,18,19,20,28,37,46,55,64,73}
        actual_neighbors = set(_get_neighbors(1))
        print("Expected neighbors: " + str(expected_neighbors))
        print("Generated neighbors: "+ str(actual_neighbors))
        self.assertEqual(actual_neighbors, expected_neighbors)

        square = 9
        print("Testing square=9")
        expected_neighbors = {0,1,2,9,10,11,18,19,20,12,13,14,15,16,17,27,36,45,54,63,72}
        actual_neighbors = set(_get_neighbors(9))
        print("Expected neighbors: " + str(expected_neighbors))
        print("Generated neighbors: "+ str(actual_neighbors))
        self.assertEqual(actual_neighbors, expected_neighbors)

        square = 31
        print("Testing square=31")
        expected_neighbors = {27,28,29,30,31,32,33,34,35,4,13,22,40,49,58,67,76,39,41,48,50}
        actual_neighbors = set(_get_neighbors(31))
        print("Expected neighbors: " + str(expected_neighbors))
        print("Generated neighbors: "+ str(actual_neighbors))
        self.assertEqual(actual_neighbors, expected_neighbors)

        square = 7
        print("Testing square=7")
        expected_neighbors = {0,1,2,3,4,5,6,7,8,16,25,34,43,52,61,70,79,15,17,24,26}
        actual_neighbors = set(_get_neighbors(7))
        print("Expected neighbors: " + str(expected_neighbors))
        print("Generated neighbors: "+ str(actual_neighbors))
        self.assertEqual(actual_neighbors, expected_neighbors)

if __name__ == "__main__":
    unittest.main()