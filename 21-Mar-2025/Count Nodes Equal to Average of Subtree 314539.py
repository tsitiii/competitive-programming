# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt  = 0
        num = 0
        def aveg(node):
            nonlocal cnt
            nonlocal num
            if node is None:
                return 0, 0
            # if node.left is None and node.right is None:
            #     i=1
            
            left ,il = aveg(node.left)
            right,ir = aveg(node.right) 
            i=il+ir+1

            total = node.val + left + right
            if total // i == node.val:
                cnt += 1
            print(total)
            # if total/cnt == root.val:
            #     num += 1
            return total,i
        aveg(root)
        return cnt

            