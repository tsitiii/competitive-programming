# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        n =  len(nums)
        low = 0
        high = n-1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res[0] = mid
                high = mid - 1 
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res[1] = mid
                low = mid + 1  
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return res

