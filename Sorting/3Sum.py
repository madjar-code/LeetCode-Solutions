from typing import (
    List,
    Tuple,
    NamedTuple,
)


class TripletTuple(NamedTuple):
    first_number: int
    second_number: int
    third_number: int


class Triplet:
    def __init__(self,
                 first_number: int,
                 second_number: int,
                 third_number: int) -> None:
        self._triplet = TripletTuple(first_number,
                                    second_number,
                                    third_number)
    @property
    def sum(self) -> int:
        triplet_sum: int = 0
        for number in self._triplet:
            triplet_sum += number
        return triplet_sum

    @property
    def as_tuple(self) -> Tuple[int]:
        return tuple(self._triplet)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List]:
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            first_num = nums[i]
            low = i + 1
            high = len(nums) - 1
            
            while low < high:
                second_num = nums[low]
                third_num = nums[high]
                triplet = Triplet(first_num,
                                  second_num,
                                  third_num)
                
                if triplet.sum < 0:
                    low += 1
                elif triplet.sum > 0:
                    high -= 1
                else:
                    triplets.add(triplet.as_tuple)
                    low += 1
                    high -= 1
        return list(triplets)


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    print(Solution().threeSum(nums))
