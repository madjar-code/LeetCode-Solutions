import unittest
from unittest import TestCase
from typing import (
    NamedTuple,
    NoReturn,  
)


class DataItem(NamedTuple):
    checked_string: str
    is_valid: bool


class TestChecker(TestCase):
    def setUp(self) -> None:
        self.data = [
            DataItem('aabcbc', True),
            DataItem('abcabcababcc', True),
            DataItem('abccba', False),
            DataItem('', True),
            DataItem('abc', True),
            DataItem('bca', False),
        ]

    def test_correct_data(self) -> None | NoReturn:
        solution = Solution()
        for data_item in self.data:
            real_flag: bool = solution.isValid(data_item.checked_string)
            self.assertIsInstance(real_flag, bool)
            self.assertEqual(real_flag, data_item.is_valid)


BASE_STRING = 'abc'
BASE_LENGTH = len(BASE_STRING)


class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if BASE_STRING in s:
                s = s.replace(BASE_STRING, '')
            elif s == '':
                return True
            else:
                return False


if __name__ == '__main__':
    unittest.main()
