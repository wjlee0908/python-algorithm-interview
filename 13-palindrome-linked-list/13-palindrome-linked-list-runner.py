import collections
from typing import Optional, Deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 앞쪽 절반을 역순으로 저장할 리스트의 head
        reverse_head = None

        # slow runner, fast runner
        # fast는 노드 두 개씩 순회한다
        slow = fast = head

        # Fast Runner를 이용해서 중간까지 간다
        # reverse linked list 구성
        while fast and fast.next:
            fast = fast.next.next
            reverse_head, reverse_head.next, slow = slow, reverse_head, slow.next

        # 리스트가 홀수 개일 때
        # fast는 두 칸씩 이동했기 때문에 not fast.next 조건으로 끝났으면 홀수 개다
        if fast:
            slow = slow.next # 중간 노드 건너뛰기

        # reverse와 리스트 뒷부분 비교하며 palindrome 확인
        # slow는 중간 노드 (뒷부분의 시작) 까지 온 상태
        reverse_iter = reverse_head
        while reverse_iter and reverse_iter.val == slow.val:
            slow, reverse_iter = slow.next, reverse_iter.next

        # 끝까지 갔으면 True
        return not reverse_iter