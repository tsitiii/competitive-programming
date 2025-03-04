# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 0
        arr = sorted(nums, reverse = True)
        mx = 0
        for i in range(len(arr)-2):
            if arr[i] < (arr[i+1] + arr[i+2]):
                ans = arr[i]+ arr[i+1] + arr[i+2]
                mx = max(mx, ans)
        return mx

        