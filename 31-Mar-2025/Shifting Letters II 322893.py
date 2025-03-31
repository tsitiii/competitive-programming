# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)  
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1
        shift = 0
        shift_values = []
        for i in range(n):
            shift += diff[i]
            shift_values.append(shift)
        result = []
        for i in range(n):
            new_char = chr(((ord(s[i]) - ord('a') + shift_values[i]) % 26) + ord('a'))
            result.append(new_char)
        
        return "".join(result)