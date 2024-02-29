from typing import List


def reverseString(self, s: List[str]):
    left, right = 0, len(s) - 1
    # two pointer
    while left < right:
        # swap
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1