# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            new = word[:i] + word[i+1:]
            freq = Counter(new)
            if len(set(freq.values())) == 1:
                return True
        return False