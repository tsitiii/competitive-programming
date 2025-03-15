# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minimum(node):
            curr = node
            while curr:
                curr = curr.left
            return curr
        if root is None:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
            return root
        elif key == root.val:
            root.val = key
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp = minimum(root.right)
                root.val = temp.val# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minimum(node):
            curr = node
            while curr.left:  
                curr = curr.left
            return curr
        
        if root is None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:  
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp = minimum(root.right) 
                root.val = temp.val  
                root.right = self.deleteNode(root.right, temp.val)  
        
        return root
        