# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        def dfs(node):
            max_time = 0
            for subordinate in graph[node]:
                max_time = max(max_time, dfs(subordinate))
            return informTime[node] + max_time
        
        return dfs(headID)