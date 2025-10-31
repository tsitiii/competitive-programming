# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        def backtrack(path, counter):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    
                    backtrack(path, counter)
                    
                    path.pop()
                    counter[num] += 1
        
        from collections import Counter
        backtrack([], Counter(nums))
        return result