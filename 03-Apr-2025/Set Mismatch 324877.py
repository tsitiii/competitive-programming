# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        n = len(nums) + 1
        res = [0,0]
        for val in range(1,n):
            if val not in dic:
                res[1] = val
            elif dic[val]>1:
                res[0] = val
        return res
