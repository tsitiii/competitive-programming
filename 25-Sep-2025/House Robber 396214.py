# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def fib(n):
            if  n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0], nums[1])
            if n not in memo:
                res1 = nums[n] + fib(n-2)
                res2 = fib(n-1)
                memo[n] = max(res1, res2)
            return memo[n]
        return fib(len(nums)-1)