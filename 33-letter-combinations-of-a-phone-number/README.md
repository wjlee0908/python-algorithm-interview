## 문제 링크
https://leetcode.com/problems/letter-combinations-of-a-phone-number

## 핵심 아이디어
- 모든 조합 구하기 -> 가지치기 -> DFS
  - 기대한 결과와 길이 같아질 때 까지

## Note
- 재귀 함수에서 상태는 인자로 전달한다
  - `dfs(i + 1, path + char)`
- 누적되는 결과는 바깥 scope 변수에 저장한다ss
