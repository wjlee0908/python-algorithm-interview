## 문제 링크
https://leetcode.com/problems/swap-nodes-in-pairs

# 반복문을 이용한 풀이
## 핵심 아이디어
- 연결 리스트 스왑 -> 연결 리스트 순서 변경 -> `node.next`를 다른 노드로 연결

## Note
- `prev.next`도 같이 변경한다. `prev -> a` 에서 `prev -> b` 로 바뀌기 때문이다
- head는 첫 번째 노드였다가 스왑 후에는 두 번째 노드로 변경된다.
  - 따라서 `head` 앞에 `ListNode(None)`인 `root` 노드를 생성하고 스왑 과정에서 root가 두 번째 노드를 가리키도록 한다.