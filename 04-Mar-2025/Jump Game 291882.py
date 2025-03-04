# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        n = len(nums)
        if nums[0] == 0 and n> 1:
            return False
        elif n == 1:
            return True
        for i in range(len(nums)):
            curr = i + nums[i]
            mx = max(mx, curr)
            if i >= mx:
                return False
            elif mx >= n-1:
                return True 
            
        return False