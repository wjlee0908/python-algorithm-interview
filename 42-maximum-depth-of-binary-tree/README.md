## 문제 링크
https://leetcode.com/problems/maximum-depth-of-binary-tree

## 핵심 아이디어
- 트리의 최대 깊이 -> 트리 레벨별로 탐색하며 반복 횟수 구하기 -> BFS

## Note
- BFS 구현 방법
  1. 큐가 빌 때 까지 반복을 돌린다
  2. 큐 길이만큼 큐에서 popleft를 하고 자식 노드를 삽입하는 것을 반복한다
     - 큐 길이만큼 반복할 때 마다 트리의 한 레벨씩 탐색함
