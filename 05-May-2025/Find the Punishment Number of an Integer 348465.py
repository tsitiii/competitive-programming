# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(num: int, target: int) -> bool:
            s = str(num * num)
            
            def dfs(index: int, current_sum: int) -> bool:
                if index == len(s):
                    return current_sum == target
                
                for j in range(index, len(s)):
                    part = int(s[index:j + 1])
                    if current_sum + part > target:
                        break  
                    if dfs(j + 1, current_sum + part):
                        return True
                
                return False
            
            return dfs(0, 0)
        ans = 0
        for i in range(1, n + 1):
            if canPartition(i, i):
                ans += i * i  
        return ans
