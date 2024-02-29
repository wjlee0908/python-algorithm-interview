## 문제 링크
https://leetcode.com/problems/valid-palindrome/

## 핵심 아이디어
- Palindrome -> 양 끝 비교 -> 양 끝 pop -> deque
- Palindrome -> 뒤집으면 같다 -> 문자열 슬라이싱 `[::-1]`

## 설명
- 문자열 조작은 Python의 문자열 슬라이싱 `[::-1]` 이 가장 빠르다
- `.leftpop()`과 `pop()` 을 이용해 끝과 끝을 비교할 수 있는데, 이 경우 Deque을 쓰면 `O(1)`으로 성능이 좋다.