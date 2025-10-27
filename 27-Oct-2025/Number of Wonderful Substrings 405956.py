# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        count = [0] * 1024
        count[0] = 1
        
        prefix_mask = 0
        result = 0
        
        for char in word:

            bit = ord(char) - ord('a')
            prefix_mask ^= (1 << bit)
            result += count[prefix_mask]

            for i in range(10):
                target_mask = prefix_mask ^ (1 << i)
                result += count[target_mask]
            
            count[prefix_mask] += 1
        
        return result