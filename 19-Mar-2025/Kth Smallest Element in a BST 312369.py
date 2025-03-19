# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        stack = [root]
        result = []
        if not root:
                return []
        while stack and root:
            node= stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                result.append(node.val)
        result.sort()
        return result[k-1]

        
         
        