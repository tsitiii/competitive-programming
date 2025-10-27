# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        
        result = []
        consecutive_count = 0
        for i in range(k - 1):
            if nums[i] + 1 == nums[i + 1]:
                consecutive_count += 1
        if consecutive_count == k - 1:
            result.append(nums[k - 1])
        else:
            result.append(-1)
        for i in range(1, n - k + 1):
            if nums[i - 1] + 1 == nums[i]:
                consecutive_count -= 1

            if nums[i + k - 2] + 1 == nums[i + k - 1]:
                consecutive_count += 1
            if consecutive_count == k - 1:
                result.append(nums[i + k - 1])
            else:
                result.append(-1)
        
        return result