## 문제 링크
https://leetcode.com/problems/design-circular-deque

## 핵심 아이디어
- deque -> 앞 뒤 모두 pop 가능하다 -> Doubly Linked List로 구현
  - `head`, `tail` node로 양 끝 트래킹
  - `head`, `tail`은 `None` 이며 `right`, `left`로 끝 노드를 가리킨다

## Note
- 파이썬에서 삼항 연산자는 `A if 조건 else B`로 표현한다