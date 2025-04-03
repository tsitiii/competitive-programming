# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        dic = Counter(nums)
        n = len(nums)+1
        res = []
        for i in range(1, n):
            if i not in dic:
               res.append(i) 
        return res