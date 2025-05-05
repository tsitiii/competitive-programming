# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for src, dest in redEdges:
            graph[src].append((dest, 'red'))
        for src, dest in blueEdges:
            graph[src].append((dest, 'blue'))
        distances = [[float('inf')] * 2 for _ in range(n)]  
        distances[0][0] = 0  
        distances[0][1] = 0  
        queue = deque([(0, None)])  
        while queue:
            node, last_color = queue.popleft()

            for neighbor, color in graph[node]:
                if color != last_color and distances[neighbor][0 if color == 'red' else 1] == float('inf'):
                    distances[neighbor][0 if color == 'red' else 1] = distances[node][0 if last_color == 'red' else 1] + 1
                    queue.append((neighbor, color))
        result = [-1] * n
        for i in range(n):
            min_dist = min(distances[i][0], distances[i][1])
            if min_dist != float('inf'):
                result[i] = min_dist

        return result