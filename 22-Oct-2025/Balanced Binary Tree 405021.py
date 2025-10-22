# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return height(root) != -1
