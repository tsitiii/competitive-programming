# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque
n, m = map(int, input().split())
rail = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    rail[u][v] = True
    rail[v][u] = True

def bfs(use_railway):
    dist = [-1] * (n + 1)
    dist[1] = 0
    q = deque([1])
    
    while q:
        u = q.popleft()
        for v in range(1, n + 1):
            if v != u:
                if use_railway:
                    has_edge = rail[u][v]
                else:
                    has_edge = not rail[u][v]
                
                if has_edge and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
    return dist[n]
train_time = bfs(use_railway=True)
bus_time = bfs(use_railway=False)
if train_time == -1 or bus_time == -1:
    print(-1)
else:
    print(max(train_time, bus_time))