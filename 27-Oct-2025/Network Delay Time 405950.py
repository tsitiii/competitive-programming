# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]
        
        while heap:
            current_dist, node = heapq.heappop(heap)
            if current_dist > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        max_time = max(dist[1:])
        return max_time if max_time < float('inf') else -1