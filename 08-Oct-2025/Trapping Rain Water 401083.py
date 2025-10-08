# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += max(0, left_max - height[left])  
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += max(0, right_max - height[right])  

        return water_trapped
