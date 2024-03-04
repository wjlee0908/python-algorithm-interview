## 문제 링크
https://leetcode.com/problems/palindrome-linked-list

# Deque(Double Ended Queue) 이용한 풀이
## 핵심 아이디어
- Palindrome -> 양 끝 같다 -> 양 끝 pop -> Deque

## Note
- Linked list를 deque에 담으려면 `node.next`를 반복하면서 값을 `.append()` 하면 된다

# Runner를 이용한 풀이
## 핵심 아이디어
- Palindrome -> 뒷쪽 절반은 앞쪽 절반을 뒤집은 것과 같다 -> linked list 절반 판별 -> Runner
  - 앞쪽 절반 뒤집기 -> 절반 순회하면서 새로운 노드를 Head로 만들기

## Note
- Runner 기법
  - Linked list는 인덱스가 없기 때문에 중간에 있는 노드를 찾기 위해 2배 빠르게 이동하는 fast runner와 slow runner를 같이 사용하는 기법.
- fast를 이용해서 절반 지점까지 간다
- 절반까지 가면서 동시에 reverse list를 만들고, reverse와 남은 절반(slow)을 비교한다