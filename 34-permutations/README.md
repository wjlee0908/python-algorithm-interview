## 문제 링크
https://leetcode.com/problems/permutations

# DFS를 이용한 풀이
## 핵심 아이디어
- 모든 조합 -> 가지치기 -> DFS
- 순열은 n이 커질 때 마다 선택할 수 있는 요소가 줄어든다 -> 인자로 줄어든 요소 전달

## Note
- 재귀 함수에 다음 상태로 list를 인자로 전달할 때, 그냥 전달하면 객체를 참조하는 것이 된다. 따라서 `my_list[:]`로 복사해서 전달하자
  - 복잡한 리스트는 `deepcopy()`
- 현재 값을 외부 변수로 선언한 뒤
  - 1. 다음 상태에서 사용할 수 있도록 변형
    2. dfs 호출
    3. 1에서 변형한 것 복구 후 반복
  - 이 패턴으로 현재 트래킹하고 있는 값을 외부 변수 하나로 관리할 수 있다
- DFS에서 `return` 값을 사용하는 것 보다는 외부 변수에 트래킹하는 값, 결과 등을 저장하면 편리하다
  - 인자에는 바뀌는 상태 전달

# itertools를 이용한 풀이
## 핵심 아이디어
- 모든 순열 구하기 -> `itertools.permutations()`

## Note
- python의 itertools 모듈을 이용하면 요소를 이용해 구성할 수 있는 순열, 조합, 중복조합 리스트를 구할 수 있다
  - 리스트로 출력하려면 `list()`로 변환해 줘야 한다