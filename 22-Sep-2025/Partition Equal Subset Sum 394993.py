# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # tot = sum(nums) //2
        # memo = defaultdict(int)
        # def dp(indx,target):
        #     if indx >= indx or target <= 0:
        #         return target == 0
        #     state = (indx, target)
        #     if state not in memo:
        #         memo[state] = dp(indx + 1, target - nums[i]) or dp(indx + 1, target)
        # return sum(nums) % 2 ==0 and dp(0, s)


        n = len(nums)
        memo = defaultdict(int)
        def dp(i, target_sum):
            if i >= n or target_sum <= 0:
                return target_sum == 0
            state = (i, target_sum)
            if state not in memo:
                memo[state] = dp(i + 1, target_sum - nums[i]) or dp(i + 1, target_sum)
            # print(memo)
            return memo[state]
        return sum(nums) % 2 == 0 and dp(0, sum(nums) // 2)

        