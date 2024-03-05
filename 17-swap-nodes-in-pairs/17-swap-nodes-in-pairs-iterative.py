# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(None)
        root.next = head
        prev = root
        a = head

        while a and a.next:
            # b가 a(head)를 가리키도록 할당
            b = a.next
            a.next = b.next
            b.next = a

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음 번 비교를 위해 이동
            a = a.next
            prev = prev.next.next

        return root.next