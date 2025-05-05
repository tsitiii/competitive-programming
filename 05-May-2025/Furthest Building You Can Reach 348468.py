# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        climbs = []  

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:  
                heapq.heappush(climbs, diff)  

                if len(climbs) > ladders:
                    smallest_climb = heapq.heappop(climbs)
                    if bricks >= smallest_climb:
                        bricks -= smallest_climb
                    else:
                        return i  

        return n - 1 