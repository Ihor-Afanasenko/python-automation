import unittest
import hw_4


class TestHomework4(unittest.TestCase):

    def test_full_equal(self):
        """ Check formatting and content positive """
        out = hw_4.print_escape_table(r"\t", 'Bell (alert)')
        exp = r'|	\t	|	Bell (alert)			|'
        self.assertEqual(out, exp)

    def test_len(self):
        """ Check number of symbols """
        out = hw_4.print_escape_table(r'\a', 'Bell (alert)')
        self.assertEqual(len(out), 23)

    def test_type_output(self):
        """ Check output result type """
        out = hw_4.print_escape_table(r'\a', 'Bell (alert)')
        self.assertIsInstance(out, str)

    def test_count_number_tab(self):
        """ Check output result has count tab element when name len < 20 and len > 11 """
        out = hw_4.print_escape_table(r'\a', 'Bell (alert)')
        self.assertEqual(out.count("\t"), 6)

    def test_count_number_tab_2(self):
        """ Check output result has count element when name len < 10 or len = 11 """
        out = hw_4.print_escape_table(r'\a', 'Bell test')
        self.assertEqual(out.count("\t"), 7)

    def test_count_number_tab_3(self):
        """ Check output result has count element when name len > 20 """
        out = hw_4.print_escape_table(r'\a', 'Bell test more then 20')
        self.assertEqual(out.count("\t"), 4)

    def test_count_number_tab_4(self):
        """ Check output result has count element when name len == 20 """
        out = hw_4.print_escape_table(r'\a', 'Bell test equal test')
        self.assertEqual(out.count("\t"), 3)

    def test_count_number_tab_5(self):
        """ Check output result has count element when name len == 10 """
        out = hw_4.print_escape_table(r'\a', 'Bell test ')
        self.assertEqual(out.count("\t"), 3)

    def test_decorate_element(self):
        """ Check output result has count element | """
        out = hw_4.print_escape_table(r'\a', 'Bell (alert)')
        self.assertEqual(out.count("|"), 3)

    def test_exist_specific_symbols(self):
        """ Check output result has specific symbol for escaping \a """
        out = hw_4.print_escape_table(r'\a', 'Bell (alert)')
        self.assertIn("\\a", out)

    def test_error_types(self):
        """ Check output result has not incorrect type """
        out = hw_4.print_escape_table(r'\a', 'Bell (alert)')
        for check_type in (int, float, list, tuple, set, dict):
            self.assertNotIsInstance(out, check_type, f"Output has type {type(check_type)}")

    def test_return_not_none(self):
        """ Check output result is not None """
        self.assertIsNotNone(hw_4.print_escape_table(r'\a', 'Bell (alert)'))

    def test_not_equal(self):
        """ Check output result is not equal string """
        self.assertNotEqual(hw_4.print_escape_table(r'\a', 'Bell (alert)'), '\\a Bell (alert)')

    def test_not_in(self):
        """ Check output result is not in some string """
        self.assertNotIn('Test string', hw_4.print_escape_table(r'\a', 'Bell (alert)'))


if __name__ == "__main__":
    unittest.main(verbosity=2)
