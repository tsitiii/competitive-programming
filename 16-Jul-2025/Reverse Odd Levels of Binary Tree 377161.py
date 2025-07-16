# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            current_level = []
            if level % 2 == 1:
                nodes = list(queue)
                values = [node.val for node in nodes]
                values = values[::-1]
                for i in range(level_size):
                    nodes[i].val = values[i]
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        
        return root