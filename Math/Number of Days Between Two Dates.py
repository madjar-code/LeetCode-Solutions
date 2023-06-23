import unittest
from unittest import TestCase
from typing import (
    NamedTuple,
    TypeAlias,
    Union,
)


DeltaType: TypeAlias = int


class TwoDatesAndDelta(NamedTuple):
    date_1: str
    date_2: str
    delta: DeltaType


class TestDateDelta(TestCase):
    def setUp(self) -> None:
        self.years_and_leap_flags = [
            (1900, False),
            (1901, False),
            ('2000', True),
            (2012, True),
            ('2016', True),
        ]

        self.two_dates_list = [
            TwoDatesAndDelta(
                date_1='2019-06-29',
                date_2='2019-06-30',
                delta=1
            ),
            TwoDatesAndDelta(
                date_1='2020-01-15',
                date_2='2019-12-31',
                delta=15
            ),
            TwoDatesAndDelta(
                date_1='2009-08-18',
                date_2='2080-08-08',
                delta=25923
            ),
            
        ]

    # @unittest.skip('Already passed')
    def test_is_leap_year(self) -> None:
        for year_leap_flag in self.years_and_leap_flags:
            year, flag = year_leap_flag
            self.assertEqual(Date.is_leap_year(year), flag)

    # @unittest.skip('Is not right')
    def test_date_delta(self) -> None:
        for two_dates in self.two_dates_list:
            date_object_1 = Date(two_dates.date_1)
            date_object_2 = Date(two_dates.date_2)
        my_delta = Date.delta(date_object_1, date_object_2)
        self.assertEqual(my_delta, two_dates.delta)


class ParsedDate(NamedTuple):
    days: int
    months: int
    years: int


class Date:
    MONTHS_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date: str) -> None:
        self._date = date
        years, months, days = map(int, date.split('-'))
        self._parsed_date = ParsedDate(days, months, years)

    @property
    def parsed_date(self) -> ParsedDate:
        return self._parsed_date

    @classmethod
    def is_leap_year(cls, year: Union[str, int]) -> bool:
        year = int(year)
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @classmethod
    def delta(cls, date_object_1: 'Date', date_object_2: 'Date') -> int:
        return abs(date_object_1._days_since_1900() -\
                   date_object_2._days_since_1900())

    def _days_since_1900(self) -> int:
        days, months, years = self._parsed_date
        
        delta_days = days + int(Date.is_leap_year(years) and months > 2)
        delta_days += sum(365 + int(Date.is_leap_year(year)) for year in range(1900, years))
        delta_days += sum(self.MONTHS_DAYS[:months])
        return delta_days


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_object_1 = Date(date1)
        date_object_2 = Date(date2)
        return Date.delta(date_object_1, date_object_2)


if __name__ == '__main__':
    unittest.main()
