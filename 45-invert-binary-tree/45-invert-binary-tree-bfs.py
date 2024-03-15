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
        queue = collections.deque([root])

        while queue:
            # 1. popleft
            node = queue.popleft()
            # 부모 노드로부터 하향식 스왑
            if node:
                # 2. swap
                node.left, node.right = node.right, node.left

                # 3. append child
                queue.append(node.left)
                queue.append(node.right)

        return root