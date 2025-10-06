# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)
            Wroot = root.val + left[1] + right[1]
            Woutroot = max(left) + max(right)
            return [Wroot, Woutroot]
        return max(dfs(root))  
    