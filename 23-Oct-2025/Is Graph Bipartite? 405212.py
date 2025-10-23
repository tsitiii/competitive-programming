# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        def dfs(node):
            for ng in graph[node]:
                if color[ng] == -1:
                    color[ng] = 1 - color[node]
                    if not dfs(ng):
                        return False
                elif color[node] == color[ng]:
                    return False
            return True
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
