# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
       if not head:
         return None
       temp = head
       while temp and temp.next:
         if temp.val == temp.next.val:
            temp.next = temp.next.next
         else:
            temp = temp.next
       return head
         
         
           
          
        