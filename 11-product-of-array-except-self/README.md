## 문제 링크
https://leetcode.com/problems/product-of-array-except-self

## 핵심 아이디어
- 곱셈 결과 -> 두 부분의 곱으로 표현할 수 있다
- 곱셈을 반복하는 대신 순회하면서 곱셈 결과를 누산할 수 있다

## Note
- python의 range는 끝 값을 포함하지 않는다. 간격이 -1이면 (끝 값 - 1)을 해 주어야 한다.