## 문제 링크
https://leetcode.com/problems/combinations

# DFS를 이용한 풀이
## 핵심 아이디어
- 조합 -> 가지치기 -> DFS
- 조합 -> 순서 x, 중복 x -> 이전에 뽑은 것보다 뒤에 있는 값만 뽑는다 (오름차순 순서 고정) -> 재귀의 다음 상태로 시작 인덱스를 조정

## Note
- 지금까지 만든 결과(`elements`)는 인자로 재귀 함수에 넣어 다음 상태로 전달한다

# itertools를 이용한 풀이
## 핵심 아이디어
- 모든 조합 구하기 -> `itertools.combinations()`