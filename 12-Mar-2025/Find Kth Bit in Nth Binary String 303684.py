# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # s = "0"
        def reversee(s):
            return s[::-1]
        def invert(s):
            result = ""
            for char in s:
                if char == "0":
                    result += "1"
                else:
                    result += "0"
            return result
        def generate(n):
            if n == 1:
                return "0"
            s = generate(n-1)
            return s + "1" + reversee(invert(s))
        s = generate(n)
        return s[k-1]
