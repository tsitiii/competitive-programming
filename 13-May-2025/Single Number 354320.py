# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)
        ans = 0
        for num in dic:
            if dic[num] == 1:
                ans = num
                break
        return ans 