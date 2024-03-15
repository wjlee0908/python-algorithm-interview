## 문제 링크
https://leetcode.com/problems/invert-binary-tree

# 재귀와 swap을 이용한 풀이
## 핵심 아이디어
- 이진 트리 반전 -> 모든 노드의 서브트리를 swap -> 재귀 -> swap하고 root return

## Note
- python에서 swap은 `a, b = b, a`로 할 수 있다
- 트리 재귀에서 부모가 사용할 노드 (현재 node)는 return 값으로 넘길 수 있다
  - 노드가 없을 때는 `None` 리턴해서 구조 유지 가능

# BFS를 이용한 풀이
## 핵심 아이디어
- 이진 트리 반전 -> 모든 노드의 서브트리를 swap -> 모든 노드 탐색 -> BFS

## Note
- BFS 구현법
  1. 큐에 루트 노드를 넣는다
  2. 큐에서 popleft 한다
  3. 원하는 동작을 수행한다
  4. 큐에 자식 노드를 넣는다
  5. 큐가 빌 때 까지 반복한다

# DFS를 이용한 풀이
## 핵심 아이디어
- 이진 트리 반전 -> 모든 노드의 서브트리를 swap -> 모든 노드 탐색 -> DFS

## Note
- BFS 코드에서 큐를 스택으로 바꾸고 `.popleft()` 대신에 `.pop()`을 하면 DFS가 된다
  - 스택에서 `.pop()`되는 노드 = 마지막에 넣은 노드 = 자식 노드이기 때문이다