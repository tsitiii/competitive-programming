# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        odd = []
        for char in s:
            odd.append(int(char))
        odd = sorted(odd, reverse = True)
        app = odd[0]
        odd.remove(odd[0])
        odd.append(app)
        result = ""
        for i in range(len(odd)):
            result += str(odd[i])
        return result