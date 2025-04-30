# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        ans = []
        for i in range(len(limits)):
            row = [-val for val in grid[i]]
            heapify(row)
            for j in range(limits[i]):
                val =  ans.append(heappop(row))
        heapify(ans)
        res = []
        for _ in range(k):
            res.append(-heappop(ans))
        return sum(res)
            