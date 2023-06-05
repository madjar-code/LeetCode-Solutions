import unittest
from unittest import TestCase
from typing import (
    List,
    NamedTuple,
    TypeAlias
)


IndexPlusPair: TypeAlias = List[int]


class DataItem(NamedTuple):
    numbers: List[int]
    target: int
    indices: IndexPlusPair 


class TestTwoSum(TestCase):
    def setUp(self) -> None:
        self.cor_data_and_exp_result =\
            [
                DataItem(
                    numbers=[2, 7, 11, 15],
                    target=9,
                    indices=[1, 2]
                ),
                DataItem(
                    numbers=[2, 3, 4],
                    target=6,
                    indices=[1, 3]
                ),
                DataItem(
                    numbers=[-1, 0],
                    target=-1,
                    indices=[1, 2]
                ),
            ]
            
    def test_correct_data(self) -> None:
        solution = Solution()
        for item in self.cor_data_and_exp_result:
            result = solution.twoSum(item.numbers, item.target)
            self.assertEqual(result, item.indices)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> IndexPlusPair:
        length: int = len(numbers)
        for i in range(len(numbers)):
            complement: int = target - numbers[i]
            low = i + 1
            high = length - 1
            while high >= low:
                middle: int = (low + high) // 2
                if numbers[middle] < complement:
                    low = middle + 1
                elif numbers[middle] > complement:
                    high = middle - 1
                else:
                    return [i+1, middle+1]
        return []


if __name__ == '__main__':
    unittest.main()
