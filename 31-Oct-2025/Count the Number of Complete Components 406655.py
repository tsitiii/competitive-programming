# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        complete_count = 0
        
        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)
                k = len(component)
                is_complete = True
                
                for node in component:
                    neighbor_count = 0
                    for neighbor in graph[node]:
                        if neighbor in component:
                            neighbor_count += 1
                    if neighbor_count != k - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_count += 1
        
        return complete_count