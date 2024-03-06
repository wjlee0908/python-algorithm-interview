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

# collections.Counter .most_common() 활용 풀이
## 핵심 아이디어
- 등장 회수 -> `collections.Counter`
- k번째로 높은 빈도 -> counter `.most_common(k)`

## Note
- `zip` 함수를 이용해서 여러 개의 리스트, 튜플을 세로로 묶을 수 있다
  - ```
    zip(('a1', 'a2'),
       ('b1', 'b2'))
    => ('a1, 'b1'), ('a2', 'b2')
    ```
- python의 `*`은 unpack 연산자로, JS의 `...`과 비슷하다
  - `*[a, b] => a,b`