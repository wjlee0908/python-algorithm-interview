## 문제 링크
https://leetcode.com/problems/jewels-and-stones/

# collections.Counter 이용한 풀이
## 핵심 아이디어
- 문자열에서 n가지 문자의 개수 구하기 -> 모든 문자의 개수 구하고 해당하는 문자의 개수 합치기 -> `collections.Counter`

## Note
- `collections.Counter`를 조회할 때 없는 인덱스를 사용하면 에러가 아닌 `0`을 리턴한다

# List Comprehension을 이용한 풀이
## 핵심 아이디어
- 문자열에서 n가지 문자의 개수 구하기 -> 찾는 집합에 있는지 여부 sum

## Note
- `sum([True, False])` 는 `True`를 1로 놓고 합을 구한다
  - 이를 응용해서 리스트 중에서 조건에 일치하는 요소의 개수를 구할 수 있다