from main import sum_of_two
import unittest


class TestSumOfTwo(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sum_of_two([2, 7, 11, 15], 9), [0, 1])

    def test_2(self):
        self.assertEqual(sum_of_two([3, 2, 4], 6), [1, 2])

    def test_3(self):
        self.assertEqual(sum_of_two([3, 3], 6), [0, 1])

    def test_4(self):
        self.assertEqual(sum_of_two([3, 4], 6), [])

    def test_5(self):
        self.assertEqual(sum_of_two([4, 4], 8), [0, 1])

    def test_6(self):
        self.assertEqual(sum_of_two(4, 8), 'Nums or target - invalid Type')
        self.assertEqual(sum_of_two(4.465, 8), 'Nums or target - invalid Type')
        self.assertEqual(sum_of_two([4, 4], 8.04583), 'Nums or target - invalid Type')
        self.assertEqual(sum_of_two([4, 4], 'hello'), 'Nums or target - invalid Type')



if __name__ == '__main__':
    unittest.main()