import unittest
from unittest import TestCase
from typing import (
    Dict,
    TypeAlias,
    NamedTuple,
)
from collections import defaultdict


RomanType: TypeAlias = str
QuantityType: TypeAlias = int


class IntegerRomanPrimitives(NamedTuple):
    integer: int
    roman_primitives: Dict[RomanType, QuantityType]


class TestIntSeparator(TestCase):
    def setUp(self) -> None:
        self.correct_data = [
            IntegerRomanPrimitives(
                integer=3,
                roman_primitives={
                    'I': 3,
                }
            ),
            IntegerRomanPrimitives(
                integer=58,
                roman_primitives={
                    'L': 1,
                    'V': 1,
                    'I': 3,
                }
            ),
            IntegerRomanPrimitives(
                integer=1994,
                roman_primitives={
                    'M': 1,
                    'CM': 1,
                    'XC': 1,
                    'IV': 1,
                }
            )
        ]

    def test_separation(self) -> None:
        for int_rom_primitives in self.correct_data:
            integer, exp_roman_primitives = int_rom_primitives
            int_separator = IntSeparator(integer)
            roman_primitives = int_separator.separate()
            # print(dict(roman_primitives))
            # print(exp_roman_primitives)
            self.assertEqual(dict(roman_primitives), exp_roman_primitives)


class RomanNumRomanPrimitives(NamedTuple):
    roman_primitives: Dict[RomanType, QuantityType]
    roman: RomanType


class TestRomanSummantor(TestCase):
    def setUp(self) -> None:
        self.correct_data = [
            RomanNumRomanPrimitives(
                roman_primitives={
                    'I': 3,
                },
                roman='III'
            ),
            RomanNumRomanPrimitives(
                roman_primitives={
                    'L': 1,
                    'V': 1,
                    'I': 3,
                },
                roman='LVIII'
            ),
            RomanNumRomanPrimitives(
                roman_primitives={
                    'M': 1,
                    'CM': 1,
                    'XC': 1,
                    'IV': 1,
                },
                roman='MCMXCIV'
            )
        ]

    def test_create_roman(self) -> None:
        for rom_num_rom_primitives in self.correct_data:
            roman_primitives, exp_roman = rom_num_rom_primitives
            roman_summator = RomanSummator(roman_primitives)
            roman = roman_summator.create_roman()
            print(roman)
            self.assertEqual(roman, exp_roman)


INTEGER_ROMAN = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}


class IntSeparator:
    """
    Class for dividing an integer into roman primitives
    """
    def __init__(self, integer: int) -> None:
        self._integer = integer
        self._roman_primitives:\
            Dict[RomanType, QuantityType] = defaultdict(int)

    def separate(self) -> Dict[RomanType, QuantityType]:
        for base_integer in INTEGER_ROMAN.keys():
            while True:
                self._integer -= base_integer
                if self._integer >= 0:
                    base_roman: RomanType = INTEGER_ROMAN[base_integer]
                    self._roman_primitives[base_roman] += 1
                else:
                    self._integer += base_integer
                    break
        return self._roman_primitives


class RomanSummator:
    """
    Class for creation roman numerals by roman primitives
    """
    def __init__(self, primitive_dict: 
            Dict[RomanType, QuantityType]) -> RomanType:
        self._primitive_dict = primitive_dict
        self._roman: RomanType = ''

    def create_roman(self) -> RomanType:
        for base_roman in self._primitive_dict.keys():
            while self._primitive_dict[base_roman] > 0:
                self._roman += base_roman
                self._primitive_dict[base_roman] -= 1
        return self._roman


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_primitives = IntSeparator(num).separate()
        roman_numeral = RomanSummator(roman_primitives).create_roman()
        return roman_numeral


if __name__ == '__main__':
    unittest.main()

