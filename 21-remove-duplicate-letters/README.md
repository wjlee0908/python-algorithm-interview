## 문제 링크
https://leetcode.com/problems/remove-duplicate-letters

# 재귀 활용 풀이
## 핵심 아이디어
- 가장 작은 사전 순 -> 사전 순 작은 문자 앞에 배치 반복 -> 재귀
- every letter appears -> set 비교

## Note
- 최종 결과에 모든 문자 종류가 포함되어 있어야 하므로 `set(s)`와 일치 여부를 확인한다

# Stack 활용 풀이
## 핵심 아이디어
- 사전식 순서 최소 -> 작은 문자부터 앞에 배치 -> Increasing Monotonic Stack
  - 단, 모든 문자 포함 제약 조건을 만족해야 하므로 count = 0 이면 못 뺌
- 마지막 위치 확인 -> `collections.Counter`

## Note
- 답을 Increasing Monotonic Stack 형태로 저장한다
  - 단, 모든 문자 포함 -> 하나만 남았으면 무조건 넣는다
    - 그래서 최종 답안이 Monotonic Stack은 아니다. 규칙만 비슷.
  - 중복 없이
- `seen`은 중복을 없애기 위해 스택에 있는 값을 관리하는 set