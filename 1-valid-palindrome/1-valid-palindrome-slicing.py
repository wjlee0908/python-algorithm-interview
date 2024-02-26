# Python slicing을 이용한 풀이
# Deque보다 속도가 빠르다

import re

def isPalindrome(self, s: str) -> bool:
    s = s.lower() # 대소문자 구분 x
    s = re.sub('[^a-z0-9]', '', s) # 숫자, 알파벳 아닌 문자열 필터링

    return s == s[::-1] # 문자열 슬라이싱. 뒤집은 문자열과 비교.