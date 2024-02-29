# Two pointer

from typing import List


def trap(self, height: List[int]) -> int:
    # 빈 리스트 예외처리
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    # Two pointer
    while left < right:
        # 최대 높이 갱신. 최대 높이만큼 빗물을 담을 수 있다
        left_max, right_max = (max(height[left], left_max), max(height[right], right_max))

        # 더 높은 쪽을 향해 투 포인터 이동
        # 최대로 담을 수 있는 빗물 양 = left_max, right_max 중 작은 쪽이기 때문
        if left_max <= right_max:
            volume += left_max - height[left] # height 만큼 이미 차 있기 때문에 최댓값에서 빼줘야 함
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume