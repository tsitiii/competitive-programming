# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bst = []
        def rec(node):
            if not node:
                return
            rec(node.left)
            bst.append(node.val)
            rec(node.right)
            
        rec(root)
        def balance(start, end):
            if end - start < 0:
                return
            mid = (end+ start)//2
            return TreeNode(bst[mid],balance(start, mid - 1),balance(mid+1, end))
        return balance(0,len(bst) - 1)


            
        