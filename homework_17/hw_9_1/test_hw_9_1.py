import unittest
import hw_9_1
import random
import sys
import os


class TestHomeworkNineVersionOne(unittest.TestCase):

    def test_sum_two_numbers(self):
        """ Test two number sum """
        for i in range(20):
            number_1, number_2 = random.random() * 100, random.random() * 100
            self.assertEqual(hw_9_1.arithmetic(number_1, number_2, '+'), number_1 + number_2)

    def test_subtraction_two_numbers(self):
        """ Test two number subtraction """
        for i in range(20):
            number_1, number_2 = random.random() * 100, random.random() * 100
            self.assertEqual(hw_9_1.arithmetic(number_1, number_2, '-'), number_1 - number_2)

    def test_multiplication_two_numbers(self):
        """ Test two number multiplication """
        for i in range(20):
            number_1, number_2 = random.random() * 100, random.random() * 100
            self.assertEqual(hw_9_1.arithmetic(number_1, number_2, '*'), number_1 * number_2)

    def test_division_two_numbers(self):
        """ Test two number division """
        for i in range(20):
            number_1, number_2 = random.random() * 100, random.random() * 100
            self.assertEqual(hw_9_1.arithmetic(number_1, number_2, '/'), number_1 / number_2)

    def test_not_known_operation(self):
        """ Test not known operation """
        number_1, number_2 = random.random() * 100, random.random() * 100
        self.assertEqual(hw_9_1.arithmetic(number_1, number_2, '^'), 'Not known operation: ^')

    def test_result_is_string(self):
        """ Test result returns string """
        self.assertIsInstance(hw_9_1.arithmetic(random.random() * 100, random.random() * 100, '^'), str)

    def test_result_is_float(self):
        """ Test result returns float """
        self.assertIsInstance(hw_9_1.arithmetic(random.random() * 100, random.random() * 100, '*'), float)

    @unittest.skip('Temporary skip test example')
    def test_not_valid_string(self):
        """ Skipped test """
        number_1, number_2 = random.random(), random.random()
        self.assertEqual(hw_9_1.arithmetic(number_1, number_1, '**'), number_1 / number_2)

    @unittest.expectedFailure
    def test_wrong_second_number(self):
        """ Test skipped by failure """
        number_1, number_2 = random.random() * 100, 0
        self.assertEqual(hw_9_1.arithmetic(number_1, number_2, '/'), number_1 / number_2)

    @unittest.skipIf(sys.platform.startswith('win'), 'This test is only appropriate for POSIX-lik')
    @unittest.expectedFailure
    def test_wrong_second_number_for_skip(self):
        """ Test skipped by win platform and Failure """
        number_1, number_2 = random.random() * 100, 0
        self.assertEqual(hw_9_1.arithmetic(number_1, number_2, '/'), number_1 / number_2)

    @unittest.skipIf(not os.path.exists('logfile'), "Need the file 'logfile' to continue")
    def test_skip_if_file_not_exist(self):
        """ Test skipped if file with name 'logfile' not exist """
        number_1, number_2 = random.random() * 100, 0
        self.assertEqual(hw_9_1.arithmetic(number_1, number_2, '/'), number_1 / number_2)

    @unittest.skipUnless(os.path.exists('logfile'), "Skipped unless 'logfile' exists")
    def test_skip_unless_file_not_exist(self):
        """ Test skipped unless file with name 'logfile' not exist """
        number_1, number_2 = random.random() * 100, 0
        self.assertEqual(hw_9_1.arithmetic(number_1, number_2, '/'), number_1 / number_2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
