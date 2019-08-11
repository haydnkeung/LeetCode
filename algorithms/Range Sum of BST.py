# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Optimized Solition
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        if root:
            if L <= root.val and root.val <= R:
                sum += root.val
            if root.left and root.val > L :
                sum += self.rangeSumBST(root.left, L, R)
            if root.right and root.val < R:
                sum += self.rangeSumBST(root.right, L, R)
        return sum

# Original Solution
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if None == root:
            return 0
        sum = 0
        sum += self.rangeSumBST(root.left, L, R)
        if root.val <= R and root.val >= L:
            sum += root.val
        sum += self.rangeSumBST(root.right, L, R)
        return sum
