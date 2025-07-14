# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return []
        que = deque([root])
        l_to_r = True
        while que:
            que_len = len(que)
            lev_node = deque()
            for _ in range(que_len):
                node = que.popleft()
                if l_to_r:
                    lev_node.append(node.val)
                else:
                    lev_node.appendleft(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(list(lev_node))
            l_to_r = not l_to_r
        return ans