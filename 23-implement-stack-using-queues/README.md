## 문제 링크
https://leetcode.com/problems/implement-stack-using-queues

## 핵심 아이디어
- 스택 `top()`, `pop()` -> 큐는 첫 번째 요소에 접근할 수 있으므로 `top()`, `pop()`을 첫 번째 요소를 이용해서 구현한다
- `push()` -> 큐는 뒤로 가기 때문에 `pop()`, `push()` 반복하면서 앞에 있는 요소들 뒤로 정렬

## Note
- 파이썬의 큐는 `collections.deque()`로 구현한다