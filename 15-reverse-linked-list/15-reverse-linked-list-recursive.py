# 재귀 함수 활용 풀이
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node -> prev 연결
        def reverse(node: ListNode, prev: ListNode = None):
            # 연결할 노드 없으면 종료
            if not node:
                return prev

            # 재귀 위해서 기존 next 저장
            # node -> prev 연결
            next, node.next = node.next, prev

            # next -> node 연결
            return reverse(next, node)

        return reverse(head)