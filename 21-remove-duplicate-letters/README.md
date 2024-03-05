## 문제 링크
https://leetcode.com/problems/remove-duplicate-letters

# 재귀 활용 풀이
## 핵심 아이디어
- 가장 작은 사전 순 -> 사전 순 작은 문자 앞에 배치 반복 -> 재귀
- every letter appears -> set 비교

## Note
- 최종 결과에 모든 문자 종류가 포함되어 있어야 하므로 `set(s)`와 일치 여부를 확인한다