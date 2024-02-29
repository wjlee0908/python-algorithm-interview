## 문제 링크
https://leetcode.com/problems/reverse-string

## 핵심 아이디어
- 끝과 끝 변경 반복, 리스트 직접 조작 -> Two pointer, swap
- 리스트 뒤집기 -> `.reverse()`

## 설명
- 리스트 뒤집기는 끝과 끝 swap을 반복해서 수행할 수 있다
- 파이선 리스트 뒤집기는 `.reverse()` 함수를 이용할 수 있다
  - return 없이 리스트를 조작한다