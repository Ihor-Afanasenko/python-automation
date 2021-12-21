import unittest
import hw_9_2
import random
from logger import logger


class TestHomeworkNineSecond(unittest.TestCase):

    def test_output_result_returns_tuple(self):
        """ Test type output result """
        logger.info('This test check output type function square')
        self.assertIsInstance(hw_9_2.square(20), tuple)

    def test_output_result_returns_correct_type(self):
        """ Test type output hasn't incorrect type """
        logger.debug('Check incorrect list type')
        for check_type in [int, float, str, dict, list]:
            self.assertNotIsInstance(hw_9_2.square(100), check_type)

    def test_result_output(self):
        """ Test arithmetics output """
        logger.warning('Enter correct side length before check')
        self.assertEqual(hw_9_2.square(100), (400, 100 ** 2, 100 * 2 ** 0.5))

    def test_size_result_tuple(self):
        """ Test size result """
        logger.info('Check size result tuple')
        self.assertEqual(len(hw_9_2.square(100)), 3)

    def test_random_side_length(self):
        """ Test random side length """
        for i in range(30):
            random_number = int((random.random() - random.random()) * 100)
            if random_number <= 0:
                logger.error(f'Random number {random_number} less or equal zero')
            self.assertEqual(hw_9_2.square(random_number),
                             (4 * random_number, random_number ** 2, random_number * 2 ** 0.5))


if __name__ == '__main__':
    unittest.main(verbosity=2)
