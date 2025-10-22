# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node == destination:
                return True
            if node  in visited:
                return False
            visited.add(node)
            for ng in graph[node]:
                if dfs(ng):
                    return True
            return False
        return dfs(source)
