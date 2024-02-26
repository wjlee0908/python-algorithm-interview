# Deque(Double Ended Queue)를 활용한 풀이

import collections
from typing import Deque

def isPalindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        # 영문자와 숫자만 확인 -> alphanumeric만 deque에 넣음
        if char.isalnum():
            # 대소문자 구분 x -> 모두 소문자로 변경
            strs.append(char.lower())

    while len(strs) > 1:
        # 왼쪽에서 pop 한 값과 오른쪽에서 pop한 값이 다르면 종료
        # Deque라서 .popleft()가 O(1)이다.
        if strs.popleft() != strs.pop():
            return False

    return True