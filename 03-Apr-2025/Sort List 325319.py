# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(left, right):
            temp = left
            temp2 = right
            dummy = ListNode(0)
            temp1 = dummy
            while temp and temp2:
                if temp.val > temp2.val:
                    dummy.next = temp2
                    temp2 = temp2.next
                else:
                    dummy.next = temp
                    temp = temp.next
                dummy = dummy.next
            if temp:
                dummy.next = temp
            elif temp2:
                dummy.next = temp2
            return temp1.next

        def SortList(node):
            if not node or not node.next:
                return node
            slow  = node
            fast = node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            left = node
            right = slow.next
            slow.next = None
            lef = SortList(left)
            rig = SortList(right)
            return merge(lef, rig)
        return SortList(head)

