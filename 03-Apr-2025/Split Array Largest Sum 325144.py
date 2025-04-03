# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            curr = 0
            cut = 0
            for num in nums:
                curr += num
                
                if curr > mid:
                    cut += 1
                    curr = num
            return cut + 1 <= k
        
        high = sum(nums)
        print(high)
        low = max(nums)
        
        while low <= high:
            mid = (low + high) //2
            if check(mid):
                
                high = mid -1
            else:
                low = mid + 1
        
        return low