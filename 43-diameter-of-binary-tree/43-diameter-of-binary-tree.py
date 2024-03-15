# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            # 거리 = 왼쪽 + 오른쪽 + 2
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            # 왼쪽, 오른쪽 자식 중 큰 값으로 결정
            return max(left, right) + 1

        dfs(root)
        return self.longest