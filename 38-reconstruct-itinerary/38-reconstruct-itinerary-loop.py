import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        # 인접 리스트 구성
        for from_airport, to_airport in sorted(tickets):
            graph[from_airport].append(to_airport)

        route = []
        # DFS로 방문했던 노드들을 중간 저장
        # 나중에 꺼내서 돌아올 수 있게
        stack = ['JFK']

        while stack:
            # DFS
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            # 한 개 이상의 유효한 여정이 존재한다는 가정 때문에 막다른 길 (다음 경로가 없는 노드)는 마지막에 방문하게 된다
            # 막혔으면 stack.pop()으로 트리의 상위 노드로 올라감
            route.append(stack.pop())

        # 다시 뒤집어 방문 순 결과로
        return route[::-1]