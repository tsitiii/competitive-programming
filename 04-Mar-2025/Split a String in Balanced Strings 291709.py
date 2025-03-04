# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dic = {}
        cnt = 0
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
            if 'L' in dic and 'R' in dic:
                if dic['L'] == dic['R']:
                    cnt += 1
                    l = dic['L']
                    r = dic['R']
                    dic['L'] -= l
                    dic['R'] -= r
        return cnt