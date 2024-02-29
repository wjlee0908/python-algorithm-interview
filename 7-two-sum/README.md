## 문제 링크
https://leetcode.com/problems/two-sum/submissions/1189484097/

## 핵심 아이디어
- 덧셈 -> 뺄셈으로 바꿔서 미지수 찾기
  - i + x = target -> x = target - i
- 값의 존재 여부, 인덱스 반환 -> Hash Map (`{ value: index }`)

## 설명
- 인덱스를 찾는 문제이기 때문에 리스트를 조작하지 않는다
  - 만약 value를 찾는 문제라면 정렬 후 Two Pointer를 이용해서 더 빠르게 실행할 수 있다.
- 값의 존재 여부 + 인덱스 반환은 index Hash Map을 이용하면 `O(1)`에 수행할 수 있다