## 문제 링크
https://leetcode.com/problems/combinations

## 핵심 아이디어
- 조합 -> 가지치기 -> DFS
- 조합 -> 중복 x -> 이전에 뽑은 것보다 뒤에 있는 값만 뽑는다 -> 재귀의 다음 상태로 시작 인덱스를 조정

## Note
- 지금까지 만든 결과(`elements`)는 인자로 재귀 함수에 넣어 다음 상태로 전달한다
