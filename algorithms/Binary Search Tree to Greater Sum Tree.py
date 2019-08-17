# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right != None:
            self.bstToGst(root.right)
        self.sum += root.val
        root.val = self.sum
        if root.left != None:
            self.bstToGst(root.left)
        return root
        