import unittest
import random
import sys


class TestHomeworkNineOneVersionTwo(unittest.TestCase):

    @unittest.skipIf(sys.version_info < (3, 10, 0), 'Can only be run in higher than python 3.10')
    def test_skipped_if(self):
        import hw_9_1_2
        """ Test skipped if version Python less than 3.10 """
        number_1, number_2 = random.random() * 100, random.random() * 100
        self.assertEqual(hw_9_1_2.arithmetic(number_1, number_2, '/'), number_1 / number_2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
