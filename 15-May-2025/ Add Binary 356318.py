# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a,2)
        num2 = int(b,2)
        ans = num1 + num2
        res = bin(ans)
        return res[2:]
        