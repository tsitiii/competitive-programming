# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            u , v = edges[i]
            graph[u].append((v,succProb[i]))
            graph[v].append((u,succProb[i]))
        distances = { i:float('-inf') for i in range(n)}
        distances[start_node] = 1.0
        heap = [(-1,start_node)]
        while heap:
            dst, node = heapq.heappop(heap)
            curr = -dst
            if curr < distances[node]:
                continue
            for ng, wt in graph[node]:
                newdst = wt * curr
                if newdst > distances[ng]:
                    distances[ng] = abs(newdst)
                    heapq.heappush(heap,(-newdst, ng))
        if distances[end_node] == float('-inf'):
            return 0
        return distances[end_node]