# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split('/')
        
        for i in range(len(arr)):
            if arr[i] == "..":
                if stack:
                    stack.pop()
            elif arr[i] == "." or arr[i] == "":
                continue 
            else:
                stack.append(arr[i])
        return '/' + '/'.join(stack)