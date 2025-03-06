# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        n = len(arr)
        mx = 0
        for i in range(len(arr)):
            curr = arr[i] + arr[n-1-i]
            mx = max(mx, curr)
        return mx