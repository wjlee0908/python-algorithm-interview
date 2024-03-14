import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 인접 리스트
        graph = collections.defaultdict(list)

        # 인접 리스트 구성
        for x, y in prerequisites:
            graph[x].append(y)

        # DFS(재귀) 한 번에 방문했던 노드를 저장
        # cyclic 구조를 판단하기 위해 사용
        traced = set()
        # 수강 가능함이 확인된 노드
        # 최적화를 위해 다시 방문 x
        visited = set()

        def dfs(i):
            # cyclic 구조이면 False
            if i in traced:
                return False
            # 이 노드의 하위 노드는 수강 가능함을 이전에 확인했으면 다시 확인하지 않음
            if i in visited:
                return True

            traced.add(i)
            # 하위 노드 중 방문 불가능한 것이 있으면 False
            for y in graph[i]:
                if not dfs(y):
                    return False

            # DFS 탐색 종료 후 경로에서 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True

        # 모든 노드에 대해 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True
