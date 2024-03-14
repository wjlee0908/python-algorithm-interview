import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 방문할 노드 minheap. 소요 시간이 짧은 노드부터 방문한다
        # [(소요 시간, 정점)]
        # 초기화 - 시작 노드 k 소요 시간은 0
        node_minheap = [(0, k)]

        # 현재까지의 노드별 최소 시간
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while node_minheap:
            time, node = heapq.heappop(node_minheap)
            # minheap이기 때문에 다시 나온 값은 무시하면 된다
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(node_minheap, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1

