## 문제 링크
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree

## 핵심 아이디어
- Binary Search Tree의 노드보다 더 큰 값 -> 오른쪽 노드
  - 모든 노드 -> (오른쪽, 부모, 왼쪽) 반복 -> 오른쪽부터 운행하는 중위 순회, 재귀

## Note
- Binary Search Tree에서 대소 관계는 `오른쪽 > 부모 > 왼쪽` 이다
- 중위 순회
  - 두 번째 방문하는 노드가 중간(root) 노드
  - 오른쪽 먼저 방문하는 것과 왼쪽 먼저 방문하는 것 모두 해당
- Binary Search Tree에서 대소 관계를 물으면 BST의 특징에 대해서 생각해 보자
- 재귀 - leaf부터 탐색하기
  ```commandline
    if root:
       self.func(root.right)  
  ```
  - 조건 검사하고 바로 다음 재귀를 호출한다
