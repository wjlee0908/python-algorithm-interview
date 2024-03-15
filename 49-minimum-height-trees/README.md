## 문제 링크
https://leetcode.com/problems/minimum-height-trees

## 핵심 아이디어
- 그래프에서 최소 높이 트리 루트 찾기 -> 그래프의 중심 찾기 -> leaf 지우면서 남는 노드 찾기
- leaf -> 연결된 간선이 하나인 노드 -> 인접 리스트의 길이가 1인 노드 

## Note
- 무방향 그래프는 양방향 그래프로 표현할 수 있다
- 양방향 그래프에서 간선을 지울 때는 반대쪽도 같이 지워야 한다
- leaf를 지워 나가면 개수가 홀수일 때는 가능한 루트가 2개일 수 있