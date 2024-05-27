import unittest
from main_ukol_21_5_2024 import Task1


class TestSumNum(unittest.TestCase):
    task = Task1()
    def test_add(self):
        self.assertEqual(self.task.add(1, 1, 1), 3)
        self.assertEqual(self.task.add(-1, 1, 1), 1)
        self.assertEqual(self.task.add(-1, 1, -1), -1)

        # testování s 0
        self.assertEqual(self.task.add(0,0,0),0)
        self.assertEqual(self.task.add(0, 1, 2), 3)
        self.assertEqual(self.task.add(1, 0, 2), 3)
        self.assertEqual(self.task.add(1, 2, 0), 3)

        #testování s negativními čísly
        self.assertEqual(self.task.add(-1,-2,-3),-6)
        self.assertEqual(self.task.add(0,-1,1),0)

        self.assertEqual(self.task.add(-1,0,1),0)
    def test_multiple_numbers(self):
        self.assertEqual(self.task.multiply(1,1,1),1)

        #testování s 0
        self.assertEqual(self.task.multiply(0,1,2),0)
        self.assertEqual(self.task.multiply(1, 0, 2), 0)
        self.assertEqual(self.task.multiply(1, 2, 0), 0)

        #testování s negativními čísly
        self.assertEqual(self.task.multiply(-1, 2, 3), -6)
        self.assertEqual(self.task.multiply(-1, -2, 3), 6)
        self.assertEqual(self.task.multiply(-1,-2,-3),-6)

    def test_not_equal(self):
        self.assertNotEqual(self.task.add(1,2,3),10)
        self.assertNotEqual(self.task.multiply(1,2,3),10)

    def test_true_false(self):
        self.assertTrue(self.task.add(1,2,3) == 6)
        self.assertFalse(self.task.add(1, 2, 3) == 7)
        self.assertTrue(self.task.multiply(1, 2, 3) == 6)
        self.assertFalse(self.task.multiply(1, 2, 3) == 7)

if __name__ == '__main__':
    unittest.main()