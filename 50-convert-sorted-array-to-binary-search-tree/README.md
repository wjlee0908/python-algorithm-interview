## 문제 링크
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

## 핵심 아이디어
- 이진 탐색 트리, 높이 균형 -> 정렬된 리스트에서 가운데 값
  - 다음 값은 subtree 재귀적으로 가운데 값

## Note
- 재귀로 트리 만들기
  1. node 생성
  2. `node.left = `, `node.right = `재귀 호출
  3. `return node`