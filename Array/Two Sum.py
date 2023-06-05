import unittest
from unittest import TestCase
from typing import (
    List,
    Dict,
    NamedTuple,
    TypeAlias
)


IndexPair: TypeAlias = List[int]


class DataItem(NamedTuple):
    numbers: List[int]
    target: int
    indices: IndexPair 


class TestTwoSum(TestCase):
    def setUp(self) -> None:
        self.cor_data_and_exp_result =\
            [
                DataItem(
                    numbers=[2, 7, 11, 15],
                    target=9,
                    indices=[0, 1]
                ),
                DataItem(
                    numbers=[3, 2, 4],
                    target=6,
                    indices=[1, 2]
                ),
                DataItem(
                    numbers=[3, 3],
                    target=6,
                    indices=[0, 1]
                ),
            ]
            
    def test_correct_data(self) -> None:
        solution = Solution()
        for item in self.cor_data_and_exp_result:
            result = solution.twoSumFast(item.numbers, item.target)
            self.assertEqual(result, item.indices)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> IndexPair:
        for i in range(len(nums)):
            complement: int = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == complement:
                    return [i, j]
        return []

    def twoSumFast(self, nums: List[int], target: int) -> IndexPair:
        num_dict: Dict[int, int] = {}
        for i, num in enumerate(nums):
            complenent: int = target - num
            if complenent in num_dict:
                return [num_dict[complenent], i]
            num_dict[num] = i
        return []


if __name__ == '__main__':
    unittest.main()