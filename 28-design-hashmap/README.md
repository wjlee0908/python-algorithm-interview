## 문제 링크
https://leetcode.com/problems/design-hashmap

## 핵심 아이디어
- Hash Map -> 해싱으로 인덱스 구하고, 충돌하면 해당 인덱스에 연결 리스트
  - 인덱스를 먼저 구하고 다음 일치하는 키를 찾는다
  - hashing: modulo - `key % self.size`

## Note
- `collections.defaultdict()` 은 존재하지 않는 값을 조회하면 에러 대신 기본 생성자로 노드를 만드니 `is None` 비교할 때 유의
  - 대신 `node.value is None`