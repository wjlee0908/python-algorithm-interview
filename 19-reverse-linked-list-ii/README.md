## 문제 링크
https://leetcode.com/problems/reverse-linked-list-ii

## 핵심 아이디어
- linked list 역순 변경 -> 노드 swap 반복

## Note
- 리스트 순서 변경은 바뀌는 노드의 앞, 뒤 노드까지 고려하자
- 첫 노드가 두 번째 노드로 swap될 수 있으니 head 앞에 root를 만들고 root.next를 head로 지정하자
  - 반복문에 똑같은 로직을 적용할 수 있다