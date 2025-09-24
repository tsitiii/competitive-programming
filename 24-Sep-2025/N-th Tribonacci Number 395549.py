# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(indx):
            if indx == 0:
                return 0
            if indx == 1 or indx == 2:
                return 1
            if indx not in memo:
                memo[indx] = dp(indx - 1) + dp(indx - 2) + dp(indx - 3)
            return memo[indx]
        res = dp(n)
        return res