from enum import Enum
from typing import List


class ColorType(int, Enum):
    RED = 0
    WHITE = 1
    BLUE = 2


class Solution:
    def sortColors(self, nums: List[ColorType]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        low, high = 0, length - 1
        i = 0
        
        while i <= high:
            if nums[i] == ColorType.RED:
                nums[i], nums[low] = nums[low], nums[i]
                i += 1
                low += 1
            elif nums[i] == ColorType.BLUE:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            else:
                i += 1
