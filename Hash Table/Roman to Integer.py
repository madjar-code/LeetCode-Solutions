import unittest
from unittest import TestCase
from typing import (
    NamedTuple,
)


class RomanInteger(NamedTuple):
    roman: str
    integer: int


class TestTranslation(TestCase):
    def setUp(self) -> None:
        self.roman_integer_list = [
            RomanInteger('III', 3),
            RomanInteger('LVIII', 58),
            RomanInteger('MCMXCIV', 1994),
        ]

    def test_translation_correct_data(self) -> None:
        solution =Solution()
        for roman_integer in self.roman_integer_list:
            roman, exp_integer = roman_integer
            integer = solution.romanToInt(roman)
            self.assertEqual(integer, exp_integer, 'Incorrect Translation')


class Solution:
    ROMAN_INTEGER = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        result_integer: int = 0
        roman_length = len(s)

        for i in range(roman_length - 1):
            current_value: int = self.ROMAN_INTEGER[s[i]]
            next_value: int = self.ROMAN_INTEGER[s[i+1]]
            if current_value < next_value:
                result_integer -= current_value
            else:
                result_integer += current_value
        last_value = self.ROMAN_INTEGER[s[-1]]
        return result_integer + last_value


if __name__ == '__main__':
    unittest.main()
