# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        currxor = 0
        for indx, num in enumerate(nums):
            total ^= num
            currxor ^= indx+1
        return total^currxor
