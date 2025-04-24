# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rever = [[] for _ in range(len(graph))]
        indegree = [0] * len(graph)
        res = []
        for u in range(len(graph)):
            for v in graph[u]:
                rever[v].append(u)
            indegree[u] = len(graph[u])
        que = deque(i for i in range(len(indegree)) if indegree[i] == 0)
        while que:
            node = que.popleft()
            for ng in rever[node]:
                indegree[ng] -= 1
                if indegree[ng] == 0:
                    que.append(ng)
        for i in range(len(indegree)):
            if indegree[i] == 0:
                res.append(i)
        return res
        
        
