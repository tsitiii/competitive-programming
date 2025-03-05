# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def processString(self, s):
        stack = []
        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
    def backspaceCompare(self, s, t):
        return self.processString(s) == self.processString(t)
