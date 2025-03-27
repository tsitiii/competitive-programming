# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        low=0
        high=len(queries)
        def check(mid,nums):
            diff = [0]* (len(nums) +1)
            for i in range(mid):
                left,right,val=queries[i]
                diff[left] += val
                diff[right + 1] -= val
            for i in range(1,len(diff)):
                diff[i]+=diff[i-1]

            
            for i in range(len(nums)):
                if nums[i] - diff[i] >0:
                    return False
            return True

        ans=-1
        while low<=high:
            mid=(low+high)//2
            if check(mid,nums):
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans
        