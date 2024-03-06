## 문제 링크
https://leetcode.com/problems/merge-k-sorted-lists

## 핵심 아이디어
- 정렬된 리스트 병합 -> k개 중 최댓값 뽑기 반복 -> Priority Queue(heapq)

## Note
- 파이썬의 Priority Queue는 리스트로 선언하고 `heapq.heappush(heap, val)`, `heapq.heappop(heap)` 형태로 표현한다
  - min heap이기 때문에 순서를 바꾸려면 튜플 형태로 인덱스를 설정해 줘야 한다
- `heapq.heappush()`를 할 때 값이 중복되면 에러가 발생하므로 이를 방지하기 위해서 인덱스와 노드를 tuple로 만들 수 있다.