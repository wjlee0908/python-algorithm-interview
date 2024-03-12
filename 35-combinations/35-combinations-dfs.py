from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            """
            답안 후보(elements)에 값을 추가하고
            뽑은 요소의 뒤에 있는 요소를 k-1개 뽑게 재귀 호출한다
            뽑을 개수가 없으면 답안에 후보를 추가하고 종료한다
            """
            if k == 0:
                results.append(elements[:])
                return

            # start부터 뽑음 - 중복 방지
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results
