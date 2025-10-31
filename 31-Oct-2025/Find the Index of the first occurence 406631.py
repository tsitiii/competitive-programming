# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0    
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i     
        return -1