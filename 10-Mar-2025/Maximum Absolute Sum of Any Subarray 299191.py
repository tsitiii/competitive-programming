# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx_curr = nums[0]
        mx_global = nums[0]
        min_curr = min_global = nums[0]

        for i in range(1,len(nums)):
            mx_curr = max(mx_curr + nums[i], nums[i])
            mx_global = max(mx_global, mx_curr)

            min_curr = min(nums[i], min_curr + nums[i])
            min_global = min(min_global, min_curr)

        return max(mx_global, -min_global)