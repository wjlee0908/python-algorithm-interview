import collections
from typing import Optional, Deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        deque: Deque = collections.deque()

        if not head:
            return True

        # linked list 순회하면서 deque에 할당
        node = head
        while node is not None:
            deque.append(node.val)
            node = node.next

        # deque 시작, 끝 pop 하면서 비교
        while len(deque) > 1:
            if deque.popleft() != deque.pop():
                return False

        return True