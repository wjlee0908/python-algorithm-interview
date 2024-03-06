## 문제 링크
https://leetcode.com/problems/longest-substring-without-repeating-characters

## 핵심 아이디어
- substring -> 문자열 안에서 연속된 결과 -> sliding window
- 중복 확인, 제거 -> hashMap에 value: index 저장하여 value의 등장 여부와 위치를 저장
  - 포인터를 index 다음 값으로 옮겨 중복 제거

## Note
- 에러가 나면 반복문 들여쓰기를 확인해 보자