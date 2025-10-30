# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**15
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for o, c, co in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], co)
        for k in range(26):
            for i in range(26):
                if dist[i][k] < INF:
                    for j in range(26):
                        if dist[k][j] < INF:
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]
            
        return total