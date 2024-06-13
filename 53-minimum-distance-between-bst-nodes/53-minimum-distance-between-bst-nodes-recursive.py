# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 차이를 구하기 위해 트래킹
    prev = -sys.maxsize
    min_diff = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """
        중위 순회
        왼쪽, 루트, 오른쪽 순
        """
        if root.left:
            self.minDiffInBST(root.left)

        # 이전에 순회한 값과 차이 구하기
        # (왼쪽 -> 루트 -> 오른쪽) -> 루트...
        # (루트 - 왼쪽), (오른쪽 - 루트), (상위 트리 루트 - 오른쪽)
        self.min_diff = min(self.min_diff, root.val - self.prev)
        self.prev = root.val

        # 오른쪽 서브트리
        if root.right:
            self.minDiffInBST(root.right)

        return self.min_diff

