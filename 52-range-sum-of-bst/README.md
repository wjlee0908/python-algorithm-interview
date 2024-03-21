## 문제 링크
https://leetcode.com/problems/range-sum-of-bst/

## DFS를 이용한 풀이
## 핵심 아이디어
- 트리에서 A 이상 B 이하인 노드 -> 모든 노드 탐색 -> DFS 재귀
  - 이진 탐색 트리, 대소 관계 -> 범위 벗어나면 left / right 탐색 중지 -> if로 재귀 가지치기

## Note
- 재귀에서 합 구하기
  ```commandline
    return node.val + dfs()
  ```
  - 점화식으로 생각
  - 이번 노드 건너뛰기
  ```commandline
    return dfs()
  ```
    - 다음 재귀 값을 그대로 리턴하기 때문에 이번 노드는 더하지 않게 된다