# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def can_cover(radius):
            i = j = 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= radius:
                    i += 1
                else:
                    j += 1
            return i == len(houses)
        
        left, right = 0, 10**9
        while left < right:
            mid = (left + right) // 2
            if can_cover(mid):
                right = mid
            else:
                left = mid + 1
        
        return left