## 문제 링크
https://leetcode.com/problems/reorder-data-in-log-files

## 핵심 아이디어
- 분류 A가 분류 B보다 앞에 온다 -> 분류 후 정렬
- xx는 순서에 영향을 끼치지 않는다 -> sort key 설정
- 동일할 경우 xx 순으로 한다 -> sort key를 tuple로 지정해서 정렬 기준 순서대로 튜플 리턴

## 설명
- `.sort()`는 `key=`에 리스트 요소를 정렬 키로 매핑시켜서 정렬시킬 수 있다
  - 튜플을 리턴하여 여러 개의 정렬 기준을 순서대로 표현할 수 있다
- 람다식은 JS의 익명 함수와 비슷한 것이다
  - `lambda x: x + 1` 이런 모양으로 쓴다