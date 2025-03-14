# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            stack = [root]
            result = []
            if not root:
                return []
            while stack and root:
                node= stack.pop()
                if node:
                    result.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)
            return result
            # print(root)
            