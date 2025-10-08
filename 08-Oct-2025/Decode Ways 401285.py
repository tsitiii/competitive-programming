# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        else:
            memo = {}
            def dp(indx):
                if indx == len(s):
                    return 1
                if indx not in memo:
                    one = 0
                    two = 0
                    if s[indx] == '0':
                        return 0
                    if indx + 1 <= len(s):
                        one = dp(indx + 1)
                    if indx + 2 <= len(s):
                        if 10 <= int(s[indx:indx+2]) <= 26:
                            two = dp(indx+2)
                    memo[indx] = one + two
                return memo[indx]
        return dp(0)