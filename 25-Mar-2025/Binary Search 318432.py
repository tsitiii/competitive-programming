# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) -1
        low = 0
        high = n
        while low <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
        else:
            return -1