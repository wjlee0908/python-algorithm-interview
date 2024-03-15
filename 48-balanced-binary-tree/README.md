## 문제 링크
https://leetcode.com/problems/balanced-binary-tree

## 핵심 아이디어
- 균형 이진 트리 -> 모든 노드에서 서브 트리 간 높이 차 1 이하 판단 -> DFS(재귀)로 높이 구하기
  - 한 번 실패하면 실패 결과(-1) 재귀적으로 위로 리턴
  - 하위 노드에 실패 있으면 실패 리턴

## Note
- 재귀 함수에서 값 누산 
    ```
    if not node:
        return 0  
  
    return fn() + 1
    ```
    - leaf는 0이고 상위 노드로 갈 수록 값이 1씩 커짐