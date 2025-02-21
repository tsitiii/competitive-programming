# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        end = None
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        cnt2 = cnt - n
        if cnt2 == 0:
            return head.next
        curr = head
        for _ in range(cnt2-1):
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
        return head
        

         