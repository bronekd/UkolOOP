import unittest
from main_ukol_21_5_2024 import Task1


class TestSumNum(unittest.TestCase):
    task = Task1()
    def test_addition(self):
        self.assertEqual(self.task.add(1, 1, 1), 3)
        self.assertEqual(self.task.add(-1, 1, 1), 1)
        self.assertEqual(self.task.add(-1, 1, -1), -1)


if __name__ == '__main__':
    unittest.main()