# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        def fibb(num):
            if num == 0 or num == 1:
                return num
            if num not in memo:
                memo[num] = fibb(num-1) + fibb(num-2)

            return memo[num]
        result = fibb(n)
        print(result)
        return result