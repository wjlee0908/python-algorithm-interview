import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            # 1. pop
            node = stack.pop()
            # 부모 노드로부터 하향식 스왑
            if node:
                # 2. swap
                node.left, node.right = node.right, node.left

                # 3. append child
                stack.append(node.left)
                stack.append(node.right)

        return root