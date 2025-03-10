# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        cnt = 1
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                cnt += 1
                end = points[i][1]
        return cnt

            