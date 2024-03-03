from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    out = []
    product = 1

    # i의 왼쪽을 곱한 값 저장
    for i in range(0, len(nums)):
        out.append(product) # append 먼저
        product *= nums[i]

    product = 1

    # product에 오른쪽 값을 곱한 결과 저장
    # 이전까지의 product를 결과에 곱한다
    # range에서 끝 값은 포함하지 않으므로 0 - 1 을 해 준다
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] *= product
        product *= nums[i]

    return out
