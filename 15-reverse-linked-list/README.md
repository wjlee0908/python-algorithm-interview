## 문제 링크
https://leetcode.com/problems/reverse-linked-list

# 재귀 활용 풀이
## 핵심 아이디어
- 연결 리스트 뒤집기 -> `node -> prev` 반복 -> 재귀 

## Note
- 처음 실행할 때는 prev를 `None`으로 설정한다
- 끝낼 때는 `-> prev`이므로 `return prev`를 한다