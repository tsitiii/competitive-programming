# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0

            if src == dst:
                return 1.0
            queue = deque([(src, 1.0)])
            visited = set()
            visited.add(src)
            
            while queue:
                node, curr_val = queue.popleft()
                
                for neighbor, val in graph[node]:
                    if neighbor == dst:
                        return curr_val * val
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_val * val))
            return -1.0
        
        return [bfs(a, b) for a, b in queries]