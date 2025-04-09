# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        cnt = 0
        def dfs(node, graph,visited):
            visited[node] = True
            for ng in range(len(graph)):
                if graph[node][ng] == 1 and not visited[ng]:
                    dfs(ng, graph, visited)
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i, isConnected, visited)
                cnt += 1
        return cnt