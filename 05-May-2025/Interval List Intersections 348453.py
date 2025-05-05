# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = 0 
        j = 0  

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            start_intersect = max(start1, start2)
            end_intersect = min(end1, end2)
            if start_intersect <= end_intersect:
                result.append([start_intersect, end_intersect])
            if end1 < end2:
                i += 1
            else:
                j += 1

        return result