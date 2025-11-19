# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p
        if rem == 0:
            return 0
        
        prefix = 0
        last_seen = {0: -1}
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            need = (prefix - rem + p) % p
            if need in last_seen:
                min_len = min(min_len, i - last_seen[need])
            last_seen[prefix] = i
        
        return min_len if min_len < len(nums) else -1