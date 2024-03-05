## 문제 링크
https://leetcode.com/problems/odd-even-linked-list/

## 핵심 아이디어
- 홀수, 짝수 구분 & 공간 복잡도 O(1) -> `odd`, `even` 각자 변수로 트래킹

## Note
- 제약 조건에 따라 `odd`, `next`가 각각 두 칸 뒤의 노드를 가리키도록 할당한 뒤 `odd.next -> even_head`로 연결한다