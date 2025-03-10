# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        curr = head
        while length >= k:
            prev = None
            tail = curr 
            for _ in range(k):  
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            prev_group.next = prev
            tail.next = curr  
            prev_group = tail
            length -= k

        return dummy.next
