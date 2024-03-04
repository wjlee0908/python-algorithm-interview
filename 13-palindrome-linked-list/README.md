## 문제 링크
https://leetcode.com/problems/palindrome-linked-list

# Deque(Double Ended Queue) 이용한 풀이
## 핵심 아이디어
- Palindrome -> 양 끝 같다 -> 양 끝 pop -> Deque

## Note
- Linked list를 deque에 담으려면 `node.next`를 반복하면서 값을 `.append()` 하면 된다

