import unittest
from unittest import TestCase
from typing import (
    NamedTuple,
    Tuple,
    List,
)


class DataItem(NamedTuple):
    numbers: List[int]
    result_number: str


class TestLargestNumber(TestCase):
    def setUp(self) -> None:
        self.cor_data_and_exp_result: List[DataItem] =\
            [
                DataItem(
                    numbers=[10, 2],
                    result_number="210"
                ),
                DataItem(
                    numbers=[3, 30, 34, 5, 9],
                    result_number="9534330"
                ),
                DataItem(
                    numbers=[0, 0],
                    result_number='0'
                )
            ]

    def test_correct_data(self):
        solution = Solution() # or AlternativeSolution
        for data_item in self.cor_data_and_exp_result:
            self.assertEqual(solution.largestNumber(data_item.numbers),
                             data_item.result_number)


class Solution:
    def _compare_two_nums(self, id_1: int, id_2: int,
                          nums: List[int]) -> Tuple[int, int]:
        num_str_1: str = str(nums[id_1]) + str(nums[id_2])
        num_str_2: str = str(nums[id_2]) + str(nums[id_1])
        if num_str_1 > num_str_2:
            return id_1, id_2
        return id_2, id_1

    def largestNumber(self, nums: List[int]) -> str:
        length: int = len(nums) 
        for i in range(length):
            for j in range(length-i-1):
                k, l = self._compare_two_nums(j, j+1, nums)
                nums[j], nums[j+1] = nums[k], nums[l]

        largest_num: str = ''.join(map(str, nums))
        
        return '0' if largest_num[0] == '0' else largest_num


class LargerNumber(str):
    def __lt__(x: str, y: str) -> bool:
        return x + y > y + x


class AlternativeSolution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=LargerNumber)
        largest_num = ''.join(nums)
        return "0" if largest_num[0] == "0" else largest_num


if __name__ == '__main__':
    unittest.main()
