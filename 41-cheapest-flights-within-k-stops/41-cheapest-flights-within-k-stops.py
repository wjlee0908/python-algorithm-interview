import collections
import heapq
import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 노드 별 (누적 가격, 남은 경유지 수)
        weights = [(sys.maxsize, k)] * n

        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # minheap - 경로를 저장해서 가장 작은 순으로 pop한다
        # [(가격, 정점, 남은 경유지 수)]
        node_minheap = [(0, src, k)]

        # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
        while node_minheap:
            price, node, num_remained_stop = heapq.heappop(node_minheap)
            # 목표지까지 최솟값 구함
            if node == dst:
                return price
            # 경유지 수가 k보다 작을 때만 heap push 진행
            if num_remained_stop >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    # 조건에 맞을 때만 push해서 최적화
                    if alt < weights[v][0] or num_remained_stop -1 >= weights[v][1]:
                        weights[v] = (alt, num_remained_stop - 1)
                        heapq.heappush(node_minheap, (alt, v, num_remained_stop - 1))

        return -1