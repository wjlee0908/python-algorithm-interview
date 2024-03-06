## 문제 링크
https://leetcode.com/problems/top-k-frequent-elements

# heapq 활용한 풀이
## 핵심 아이디어
- k번째로 큰 -> heapq pop 이용하면 O(1) * k 시간에 가능
- 등장 회수 -> `collections.Counter`

## Note
- 힙 생성
  - list 만들고 `heapq.heappush(l, value)` 반복
  - 파이썬 heapq는 min heap이기 때문에 max heap으로 만드려면 `(-key, val)` 형태의 튜플로 저장해야 한다
