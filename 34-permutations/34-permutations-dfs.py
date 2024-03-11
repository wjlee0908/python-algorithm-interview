from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        # 지금까지 조합한 순열
        prev_elements = []

        def dfs(elements):
            """
            elements의 요소를 하나 붙여서 만든 순열을 생성한다
            붙일 elements가 없으면(다 붙였으면) results에 만든 순열을 추가한다
            """
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                # 다음 재귀에 전달할 요소 목록
                # [1, 2, 3] -> [1,2] -> [1] -> []
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                # append 이전 상태로 돌아온 뒤 다른 요소를 붙인다
                prev_elements.pop()

        dfs(nums)
        return results
