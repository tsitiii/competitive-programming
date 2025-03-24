# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
       
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            square =  mid * mid 
            if square > x :
                high = mid -1
            elif square == x:
                return mid
            else:
                low = mid + 1
        return high

