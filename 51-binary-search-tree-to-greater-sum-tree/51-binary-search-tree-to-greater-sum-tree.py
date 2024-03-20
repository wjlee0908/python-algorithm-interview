# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    합을 누적해서 저장할 변수
    """
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        # 오른쪽 - 부모 - 왼쪽
        if root:
            self.bstToGst(root.right)

            self.val += root.val
            root.val = self.val

            self.bstToGst(root.left)

        return root