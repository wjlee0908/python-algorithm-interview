# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # 재귀적으로 swap
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            # 부모 노드에서 동작을 위해 root 리턴
            return root
        return None