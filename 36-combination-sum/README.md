## 문제 링크
https://leetcode.com/problems/combination-sum

## 핵심 아이디어
- 조합 -> 가지치기 -> DFS
- 조합 -> 같은 조합 다른 순서 x -> 주어진 순서로 고정 -> 다음 재귀에서는 뽑은 값 뒤의 값만 뽑는다
  - 중복 조합 -> 다음 재귀에서 뽑은 값도 포함
- 합이 일치하는 조합 구하기 -> 주어진 합에서 빼면서 `csum <= 0` 되면 백트래킹

## Note
- 조합은 뽑기 시작할 인덱스를 상태로 전달한다
  - 순서를 주어진 순서로 고정하기 위해서
  - 순서만 다른 조합 추가되는 것 방지