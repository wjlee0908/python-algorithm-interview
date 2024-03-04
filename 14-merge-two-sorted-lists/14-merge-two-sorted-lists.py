# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1이 작은 값이 되도록 swap
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        # 다음 노드는 재귀로 연결
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        # 작은 값이 선택됨
        return list1
