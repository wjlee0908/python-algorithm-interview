## 문제 링크
https://leetcode.com/problems/longest-palindromic-substring

## 핵심 아이디어
- 팰린드롬 -> 양 끝 비교 반복 -> Two Pointer
  - 짝수, 홀수 case 따로 확인해야 한다
- 가장 긴 부분 집합 -> 반복문 돌리면서 result 갱신

## 설명
- `while 성공조건` 문으로 첫 실패까지 반복문을 돌리고 첫 실패의 left, right 값을 이용해서 two pointer의 답을 구한다
- `max(str1, str2, key=len)` 문을 이용해서 문자열의 길이를 기준으로 최댓값을 구할 수 있다