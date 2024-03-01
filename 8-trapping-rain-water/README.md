# 문제 링크
https://leetcode.com/problems/trapping-rain-water/submissions/1189514635/

# Two Pointer 풀이
## 핵심 아이디어
- 한 칸에서의 물의 값 = 왼쪽 지역해, 오른쪽 지역해를 활용하여 결정 -> Two Pointer
- left_max, right_max 중 작은 쪽이 물의 양을 결정하기 때문에 작은 쪽을 옮기면서 물의 양을 더한다

## Note
- 가장 일반적인 case에서의 해법을 생각하고 반복하여 전체 값을 구하자
- x=n 일때 기준으로 먼저 생각해 보자
- https://www.youtube.com/watch?v=ZI2z5pq0TqA

# Monotonic Stack 풀이
## 핵심 아이디어
- 값이 작아질 때는 pass, 값이 커질 때는 이전 값 기반으로 계산 -> Decreasing Monotonic Stack
- 그래프에서 거리가 필요하면 index를 저장한다

## Note
- 값을 하나씩 추가하면서 로직을 생각해 보자
- 주어진 예시보다 단순한 예시를 만들어 보자
- https://www.youtube.com/watch?v=UMFKP9cTDtI