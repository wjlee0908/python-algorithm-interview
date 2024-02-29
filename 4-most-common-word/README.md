## 문제 링크
https://leetcode.com/problems/most-common-word

## 핵심 아이디어
- 리스트에서 가장 흔한 요소 -> 리스트 요소 개수 세기 -> `collections.Counter()`
- 대소문자 구분 x -> 모두 소문자로 변경 -> `.lower()`
- 구두점(특수문자) 무시 -> 특수문자 제거 -> `re.sub(r'[^\w]', ' ', paragraph)`

## 설명
- List comprehension
  - JS의 `.map()`, `.filter()`와 비슷한 기능
```
even_squares = [x ** 2
    for x in list
    if x % 2 == 0]
```