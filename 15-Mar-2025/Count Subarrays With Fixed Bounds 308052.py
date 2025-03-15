# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        lastMinK = lastMaxK = lastInvalid = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                lastInvalid = i 
            if nums[i] == minK:
                lastMinK = i 
            if nums[i] == maxK:
                lastMaxK = i
            if lastMinK != -1 and lastMaxK != -1:
                count += max(0, min(lastMinK, lastMaxK) - lastInvalid)

        return count
        