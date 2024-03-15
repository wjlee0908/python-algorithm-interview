## 문제 링크
https://leetcode.com/problems/serialize-and-deserialize-binary-tree

## 핵심 아이디어
- 직렬화 결과가 트리 가로 순서 -> BFS -> queue
- 역직렬화 -> 입력이 트리 가로 순서 -> BFS -> root 노드 만들어서 queue에 넣고 시작

## Note
- 반복 구조에서는 노드 생성 전에 생성 여부를 확인해야 하는데, 이것을 배열의 index를 자식 노드 위치에서 이동하면서 확인할 수 있다

