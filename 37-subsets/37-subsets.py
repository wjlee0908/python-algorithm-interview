from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(index, path):
            # 매번 결과 추가
            results.append(path)

            # 뽑은 값 뒤에 있는 값을 뽑으며 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return results