from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    # target - n을 O(1)에 찾기 위한 hash
    # value: index
    nums_map = {}

    # (index, value) 형태로 바꾼 후 loop
    for i, num in enumerate(nums):
        # hash map에 값이 있는 지 탐색
        # O(1)
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i