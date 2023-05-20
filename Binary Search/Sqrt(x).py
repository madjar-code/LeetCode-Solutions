import unittest
from unittest import TestCase
from enum import Enum
from functools import wraps
from typing import (
    Callable,
    Optional,
    List,
    Any
)


class TestNumber(TestCase):
    def setUp(self) -> None:
        self.incorrect_values: List[Any] =\
            ['3', 1.2, -2, 'asf', []]
        self.correct_values: List[int] =\
            [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # def test_incorrect_values(self):
    #     for value in self.incorrect_values:
            # self.assertRaises(ValueError, Number, value)

    def test_int_sqrt(self):
        for value in self.correct_values:
            number = Number(value)
            print(number.get_int_sqrt())


class ErrorMessages(str, Enum):
    INCORRECT_TYPE = 'Incorrect type of value'
    NEGATIVE_VALUE = 'Number must be positive or zero'


def value_exception_handler(method: Callable):
    @wraps(wrapped=method)
    def wrapper(self: 'Number', value: Any):
        try:
            return method(self, value)
        except:
            print('Incorrect value')
    return wrapper


class Number:
    def __init__(self, value: Any) -> None:
        # self._value = value
        self._value: Optional[int] = None
        self.set_value(value)

    def get_value(self) -> int:
        return self._value

    @value_exception_handler
    def set_value(self, value: Any) -> None:
        # Retrieving value must be a natural
        if not isinstance(value, int):
            raise ValueError(ErrorMessages.INCORRECT_TYPE.value)
        if value < 0:
            raise ValueError(ErrorMessages.NEGATIVE_VALUE.value)
        self._value = value

    def get_int_sqrt(self) -> int:
        low: int = 1
        high: int = self._value
        
        mid: int = high
        
        while low <= high:
            mid = (low + high) // 2
            checked = mid ** 2
            if checked == self._value:
                return mid
            elif checked < self._value:
                low = mid + 1
            elif checked > self._value:
                high = mid - 1
        return high


class Solution:
    def mySqrt(self, x: int) -> int:
        number = Number(x)
        return number.get_int_sqrt()

if __name__ == '__main__':
    unittest.main()
