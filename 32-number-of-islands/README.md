## 문제 링크
https://leetcode.com/problems/number-of-islands

## 핵심 아이디어
- 2차원 배열에서 1 덩어리 개수 구하기 -> 연결된 1 지우고 count + 1 -> DFS 

## Note
- Python 중첩 함수에서는 바깥 scope에 접근 가능하다
  - 단 `var = xx` 형태의 재할당을 하면 로컬 변수로 취급된다
  - 따라서 재할당을 하려면 함수 내부에서 `global` 선언을 해야 한다