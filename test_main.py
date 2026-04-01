import unittest
from unittest.mock import patch
from main import calculate_sum_and_average, get_numbers_from_user

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average([1, -2, 3])

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average(["a", "b", "c"])

    @patch("builtins.input", return_value="1 2 3")
    def test_get_numbers_from_user_valid_input(self, mock_input):
        self.assertEqual(get_numbers_from_user(), [1, 2, 3])
        mock_input.assert_called_once_with("Nhập dãy số cách nhau bởi dấu cách: ")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1 a 3", "4 5 6"])
    def test_get_numbers_from_user_retries_on_non_integer(self, mock_input, mock_print):
        self.assertEqual(get_numbers_from_user(), [4, 5, 6])
        mock_print.assert_called_once()

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1 -2 3", "7 8"])
    def test_get_numbers_from_user_retries_on_non_positive(self, mock_input, mock_print):
        self.assertEqual(get_numbers_from_user(), [7, 8])
        mock_print.assert_called_once()

if __name__ == '__main__':
    unittest.main()
