import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        # Priority Queue
        freqs_heap = []

        for f in freqs:
            # 최대 빈도수가 먼저 pop되게 하기 위해서 빈도수 * -1을 key로 지정
            # python heapq는 min heap이기 때문에 순서 변경
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk