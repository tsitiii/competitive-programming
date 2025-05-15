# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        ans = num.bit_length()
        val = (1 << ans) -1
        return num ^ val 
       