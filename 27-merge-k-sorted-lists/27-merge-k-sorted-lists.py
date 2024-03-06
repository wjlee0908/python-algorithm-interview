# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i])) # 중복 에러 방지를 위해 tuple로 저장

        # 힙 pop으로 최솟값을 꺼낸다
        # 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2] # pop한 노드 연결

            result = result.next # 끝 노드로 순회
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
