
import unittest
from unittest.mock import patch, call
from euclidian import Euclidnum


class TestEuclidnum(unittest.TestCase):

    # The following tests are cases in which a >= b
    @patch('builtins.input')
    @patch('builtins.print')
    def test_b_eq_0(self, mock_print, mock_input):
        mock_input.side_effect = [5, 0]
        Euclidnum.get_numbers()
        self.assertEqual(mock_print.mock_calls, [call('the numbers are in the correct order'), call('the GCD is ', 5)])

    @patch('builtins.input')
    @patch('builtins.print')
    def test_a_b_not_int(self, mock_print, mock_input):
        mock_input.side_effect = ["5", "0"]
        Euclidnum.get_numbers()
        self.assertEqual(mock_print.mock_calls, [call('the numbers are in the correct order'), call('the GCD is ', 5)])

    @patch('builtins.input')
    @patch('builtins.print')
    def test_b_gt_0(self, mock_print, mock_input):
        mock_input.side_effect = [5, 1]
        Euclidnum.get_numbers()
        self.assertEqual(mock_print.mock_calls, [call('the numbers are in the correct order'), call('the GCD is ', 1)])

    # This mirrors case 1 but with a/b flipped to test the first if statement
    @patch('builtins.input')
    @patch('builtins.print')
    def test_a_lt_b(self, mock_print, mock_input):
        mock_input.side_effect = [0, 5]
        Euclidnum.get_numbers()
        # this should be the only call to 'print'
        self.assertEqual(mock_print.mock_calls, [call('the GCD is ', 5)])


if __name__ == '__main__':
    unittest.main()