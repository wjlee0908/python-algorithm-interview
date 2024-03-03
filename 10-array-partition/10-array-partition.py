from typing import List


def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort(reverse=True)

    for n in nums:
        # 큰 값부터 pair
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum