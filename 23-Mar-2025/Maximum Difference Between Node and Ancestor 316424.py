# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, cur_min, cur_max):
            if not node:
                # At a leaf, the difference between the current max and min is our candidate answer.
                return cur_max - cur_min
            
            # Update the current min and max with the current node's value.
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            
            # Recurse for left and right children.
            left_diff = dfs(node.left, cur_min, cur_max)
            right_diff = dfs(node.right, cur_min, cur_max)
            
            # Return the maximum difference found.
            return max(left_diff, right_diff)
        
        # Start the DFS with the root's value as both the current min and max.
        return dfs(root, root.val, root.val)
