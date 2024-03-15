## 문제 링크
https://leetcode.com/problems/merge-two-binary-trees/

## 핵심 아이디어
- 노드 값 합하기 -> 모든 노드 탐색하면서 새로운 트리 생성 -> DFS

## Note
- DFS로 새로운 트리 만들기
```commandline
    node = TreeNode()
    node.left = func()
    node.right = func()
    
    reuurn node
```