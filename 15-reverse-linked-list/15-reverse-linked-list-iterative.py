# 반복문 활용 풀이
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        # node가 None이 될 때 까지 반복
        # node -> prev 연결
        # prev = node, node = next 할당 반복
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev