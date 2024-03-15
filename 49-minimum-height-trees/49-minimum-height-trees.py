import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프를 인접 리스트로 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            # leaf는 연결된 간선이 한 개다
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때 까지 반복 제거
        while n > 2: # 짝수 개인 경우 두 개가 남을 수 있다
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf) # 양방향이므로 반대쪽에서도 제거해 준다

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves