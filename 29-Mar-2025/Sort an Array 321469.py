# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(arr):
            if len(arr) <= 1:  
                return arr
            mid = len(arr) // 2
            lefth = merge_sort(arr[:mid])  
            righth = merge_sort(arr[mid:])  
            return merge(lefth, righth)
        def merge(lefth, righth):
            ans = []
            left, right = 0, 0
            while left <len(lefth) and right < len(righth):
                if lefth[left] < righth[right]:
                    ans.append(lefth[left])
                    left += 1
                else:
                    ans.append(righth[right])
                    right += 1
            while left <len(lefth):
                ans.append(lefth[left])
                left += 1
            while right < len(righth):
                ans.append(righth[right])
                right += 1
            return ans
            
        return merge_sort(nums)

        