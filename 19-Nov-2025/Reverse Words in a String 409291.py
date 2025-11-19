# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        print(arr)
        arr = arr[::-1]
        return " ".join(arr)