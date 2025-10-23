# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        def bfs(node):
            que = deque([node])
            while que:
                currnode = que.popleft()
                for ng in graph[currnode]:
                    if color[ng] == -1:
                        color[ng] = 1- color[currnode]
                        que.append(ng)
                    elif color[ng] == color[currnode]:
                        return False
            return True
            
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = 0
                if not bfs(i):
                    return False
        return True
