# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            next_node = slow.next  
            slow.next = prev      
            prev = slow           
            slow = next_node       
        left, right = head, prev
        while right: 
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True