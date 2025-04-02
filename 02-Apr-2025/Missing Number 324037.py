# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result  = sorted(nums)
        for i in range(len(result) + 1):
            if i in result:
                continue
            else:
                return i
