# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def check(mid):
            car = 0
            for rank in ranks:
                car+= int(pow((mid/rank), 0.5))
            return car >= cars

        low = 0
        high = max(ranks) * (cars **2)
        while low <= high:
            mid = (high + low) // 2
            if check(mid):
                high = mid -1
            else:
                low = mid + 1
        return low