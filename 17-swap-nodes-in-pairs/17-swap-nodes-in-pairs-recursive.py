# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next

            # 다음 쌍 swap 후 다음 쌍의 첫 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head