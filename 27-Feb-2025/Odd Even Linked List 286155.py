# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        oddcurr = head
        oddhead = oddcurr
        evencurr = oddcurr.next
        evenhead = evencurr

        while oddcurr or evencurr:
            if oddcurr and oddcurr.next:
                oddcurr.next = oddcurr.next.next
            if oddcurr:
                if oddcurr.next == None:
                    oddcurr.next = evenhead
                    break
                oddcurr = oddcurr.next

            
            if evencurr and evencurr.next:
                evencurr.next = evencurr.next.next
            if evencurr:
                evencurr = evencurr.next
        # print(oddcurr)
        # print(evenhead)
        # print(oddhead)

        
        return oddhead

