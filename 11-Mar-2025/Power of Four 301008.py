# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def fib(n):
            if n == 1:
                return True
            elif n < 1:
                return False
            else:
                target = fib(n/4)
                return target
        return fib(n)
        
