## 문제 링크
https://leetcode.com/problems/implement-queue-using-stacks/

## 핵심 아이디어
- 큐는 스택 역순으로 `pop()` -> output 스택을 추가로 생성해서 `pop()`, `append()` 반복하면 역순으로 저장된다

## Note
- 역순으로 차례로 `pop()` 되기 때문에 `output` 스택을 초기화하지 않고 멤버로 관리해도 된다