from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            """
            candidates의 값 중에서 index~끝에 있는 값을 하나 뽑아 조합(path)에 추가한다
            이후 범위를 이미 뽑은 값의 다음 값 부터로 좁혀 재귀 호출한다
            csum = 0이 되면 답안에 추가

            :param csum: target에서 지금까지의 조합에 포함된 값을 뺀 값. 0이 될 때 까지 반복한다.
            :param index: 요소를 뽑을 시작 범위. 이미 뽑은 요소의 뒤쪽으로 좁히면서 순서를 고정한다. (순서만 다른 조합 나오는 것 방지)
            :param path: 현재 확인하고 있는 조합 후보
            """
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # index ~ 끝까지 하나씩 뽑은 것을 조합에 추가하고 범위를 좁혀서 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result