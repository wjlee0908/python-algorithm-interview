# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 예외 처리
        if not head or left == right:
            return head

        # 리스트 출력, 로직 반복을 위해 head 앞에 root 생성
        # root -> head
        root = start = ListNode(None)
        root.next = head

        # start 노드를 left의 앞 노드로 지정한다
        # (left - 1) 번째 노드의 next도 변경해야 하기 때문
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례로 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp # 인접 노드 두 개 역순으로 변경

        return root.next