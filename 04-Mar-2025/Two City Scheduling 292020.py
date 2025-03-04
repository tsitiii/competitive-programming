# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totl = 0
        costs.sort(key = lambda x : x[0] - x[1])
        n = len(costs) // 2
        for i in  range(n):
            a, b = costs[i]
            totl += a
        for i in range(n,len(costs)):
            a, b = costs[i]
            totl += b
        return totl