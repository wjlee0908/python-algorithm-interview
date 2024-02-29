## 문제 링크
https://leetcode.com/problems/group-anagrams

## 핵심 아이디어
- 애너그램 -> 순서를 바꾸면 같다 -> 정렬하면 같다 -> `.sorted()`
- 그룹핑 -> `collections.defaultdict(list)`

## 설명
- 애너그램은 정렬하면 같은 문자열이 되기 때문에 정렬한 값을 `defaultdict`의 키로 쓰고 append한다.
- `.sorted()`의 리턴 값은 리스트이기 때문에 `''.join(mylist)'`를 이용해서 리스트를 문자열로 변환한다