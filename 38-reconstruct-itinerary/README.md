## 문제 링크
https://leetcode.com/problems/reconstruct-itinerary

# DFS를 이용한 풀이
## 핵심 아이디어
- `[from, to]` 리스트 -> 그래프
- 결과가 방문하는 노드 리스트 -> 그래프 경로 -> 인접 리스트 + DFS

## Note
- 방문 경로는 인접 리스트에 DFS를 적용하여 구할 수 있다
- 인접 리스트는 `collections.defaultdict(list)`로 만든다
- 리스트의 `pop(0)`는 `O(N)`, `pop()`은 `O(1)`이기 때문에 리스트를 역순으로 구성해서 시간 복잡도를 줄일 수 있다