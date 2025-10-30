# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        first = [float('inf')] * (n + 1)
        second = [float('inf')] * (n + 1)
        queue = deque()
        queue.append((1, 0))
        first[1] = 0   
        while queue:
            node, t = queue.popleft()
            for neighbor in graph[node]:
                if (t // change) % 2 == 0:
                    arrival_time = t + time
                else:
                    wait_time = change - (t % change)
                    arrival_time = t + wait_time + time
                if arrival_time < first[neighbor]:
                    second[neighbor] = first[neighbor]
                    first[neighbor] = arrival_time
                    queue.append((neighbor, arrival_time))
                elif first[neighbor] < arrival_time < second[neighbor]:
                    second[neighbor] = arrival_time
                    queue.append((neighbor, arrival_time))
        
        return second[n]