# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u,w))

        def dijikstra(node):
            distances = [float('inf') for _ in range(n)]
            distances[node] = 0
            heap = [(0,node)]
            while heap:
                dst, node = heapq.heappop(heap)
                if dst > distances[node]:
                    continue
                for ng,wt in graph[node]:
                    newdst = wt + dst
                    if newdst <= distances[ng]:
                        distances[ng] = newdst
                        heapq.heappush(heap, (newdst,ng))
            return distances
        mincnt = float('inf')
        ansindx = -1
        for i in range(n):
            cnt = 0
            distances = dijikstra(i)
            for j in range(n):
                if j != i and distances[j] <= distanceThreshold:
                    cnt += 1
            if cnt < mincnt or (cnt == mincnt and i > ansindx):
                mincnt = cnt
                ansindx = i
        return ansindx