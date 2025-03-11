# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def zeros(n):
            if n < 5:
                return 0
            return n//5 + zeros(n//5)
        return zeros(n)