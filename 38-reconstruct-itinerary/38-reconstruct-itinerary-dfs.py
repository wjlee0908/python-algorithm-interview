import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프를 인접 리스트로 구성
        graph = collections.defaultdict(list)

        # pop() - O(1)을 위해 알파벳 먼저 오는 게 스택의 맨 위로 오도록 역순으로 리스트에 넣음
        for from_airport, to_airport in sorted(tickets, reverse=True):
            graph[from_airport].append(to_airport)

        route = []
        def dfs(airport):
            """
            airport에서 출발했을 때 도착 가능한 목적지 중에서 알파벳이 가장 앞선 목적지를 재귀로 방문합니다
            방문 후 경로에 공항을 추가합니다
            """
            # 역순 리스트의 마지막을 pop 해서 어휘 순 방문
            while graph[airport]:
                dfs(graph[airport].pop())
            route.append(airport)

        dfs('JFK')
        # dfs에서 방문 먼저 하고 route에 추가해서 역순으로 정렬되었기 때문에 다시 뒤집는다
        return route[::-1]
