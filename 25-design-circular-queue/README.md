## 문제 링크
https://leetcode.com/problems/design-circular-queue

## 핵심 아이디어
- Queue -> 뒤로 넣고 앞으로 빼야 함 -> 넣고 뺄 때 쓸 2개의 포인터 관리

## Note
- `front == rear`이면 `full` 이거나 `empty` 상태이다
  - 값 존재 여부로 `empty` 구분
