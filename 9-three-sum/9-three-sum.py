from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    # 더할 첫 번째 값 순회
    for i in range(len(nums) - 2):
        # 중복된 값 건너 뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # 더할 두 번째 값, 세 번째 값 -> Two pointer
        # 정렬된 값이므로 대소에 따라 포인터 이동
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum == 0 -> 정답 저장
                results.append([nums[i], nums[left], nums[right]])

                # 스킵 처리
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results
