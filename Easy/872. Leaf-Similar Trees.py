# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getleaf(self, node: Optional[TreeNode], l: List):
        if node.left is None and node.right is None:
            l.append(node.val)
        elif node.left is not None and node.right is None:
            self.getleaf(node.left, l)
        elif node.left is None and node.right is not None:
            self.getleaf(node.right, l)
        else:
            self.getleaf(node.left, l)
            self.getleaf(node.right, l)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1, l2 = list(), list()
        self.getleaf(root1, l1)
        self.getleaf(root2, l2)
        if l1 == l2:
            return True
        else:
            return False


        