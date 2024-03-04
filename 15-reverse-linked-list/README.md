## 문제 링크
https://leetcode.com/problems/reverse-linked-list

# 재귀 활용 풀이
## 핵심 아이디어
- 연결 리스트 뒤집기 -> `node -> prev` 반복 -> 재귀 

## Note
- 처음 실행할 때는 prev를 `None`으로 설정한다
- 끝낼 때는 `-> prev`이므로 `return prev`를 한다
- `node`를 바꾸면 `node.next`도 바뀌기 때문에 `next`는 다른 변수에 저장한다

# 반복문 활용 풀이
## 핵심 아이디어
- 연결 리스트 뒤집기 -> `node -> prev` 반복 -> 반복문

## Note
- `while`문으로 순회하는 `node`가 None이 될 때 까지 반복한다
- `node -> prev`
- `prev`, `node` 갱신