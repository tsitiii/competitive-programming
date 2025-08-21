# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        m = len(s)
        letters = []
        for i, char in enumerate(s):
            if char.isalpha():
                letters.append(i)
        k = len(letters)
        result = []
        for mask in range(1 << k):
            temp = list(s)
            for j in range(k):
                idx = letters[j]
                if mask & (1 << j):
                    temp[idx] = temp[idx].upper()
                else:
                    temp[idx] = temp[idx].lower()
            result.append(''.join(temp))
        return result