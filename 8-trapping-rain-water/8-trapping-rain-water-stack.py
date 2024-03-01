from typing import List


def trap(self, height: List[int]) -> int:
    # Decreasing Monotonic Stack
    # 막대의 index를 저장
    stack = []
    volume = 0

    for i in range(len(height)):
        # 스택의 decreasing 조건을 불만족하면 만족할 때 까지 pop 한다
        # pop 하면서 각 막대로 담을 수 있는 물 높이 계산
        while stack and height[i] > height[stack[-1]]:
            current = stack.pop()

            # 왼쪽 벽 없으면 물 저장 못 함
            if not len(stack):
                break

            left_wall_idx = stack[-1]
            left_wall_height = height[left_wall_idx]

            right_wall_height = height[i]

            distance = i - left_wall_idx - 1
            water_height = min(right_wall_height, left_wall_height) - height[current]

            volume += distance * water_height

        stack.append(i)
    return volume

