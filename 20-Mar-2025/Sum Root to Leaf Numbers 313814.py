# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def summ(val, node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return int(str(val) + str(node.val))
            num = summ(str(val) + str(node.val), node.left)
            num2 = summ(str(val) + str(node.val), node.right)
            return int(num) + int(num2)
        return summ('',root)

