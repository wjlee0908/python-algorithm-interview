## 문제 링크
https://leetcode.com/problems/add-two-numbers/

## 핵심 아이디어
- 덧셈, 역순 리스트 -> 덧셈은 작은 자리수부터 계산한다 -> linked list 순회

## Note
- 답은 root node (val=0)의 next부터 저장하고 `root.next`를 return한다
- `몫, 나머지 = divmod()` 함수를 이용하면 몫과 나머지를 함께 리턴할 수 있다
  - carry 구하기: `divmod(sum + prev_carry, 10)`