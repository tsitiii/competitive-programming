# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def check(mid):
            count = 1
            prev = position[0]
            for pos in position[1:]:
                if pos - prev >= mid:
                    count += 1
                    prev = pos
                    if count == m:
                        return True
            return count >= m
        
        low = 1
        high = position[-1] - position[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid  # This mid is valid, try for a larger one
                low = mid + 1
            else:
                high = mid - 1
        
        return ans