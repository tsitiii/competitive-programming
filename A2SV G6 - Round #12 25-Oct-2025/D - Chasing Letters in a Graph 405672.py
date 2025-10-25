# Problem: D - Chasing Letters in a Graph - https://codeforces.com/gym/606404/problem/D

import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx+1])
    idx += 2
    s = data[idx]
    idx += 1
    
    graph = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        graph[u].append(v)
        indeg[v] += 1
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(order) < n:
        print(-1)
        return
    dp = [[0] * 26 for _ in range(n)]
    ans = 0
    
    for u in order:
        letter_idx = ord(s[u]) - ord('a')
        dp[u][letter_idx] += 1
        ans = max(ans, dp[u][letter_idx])
        for v in graph[u]:
            for c in range(26):
                dp[v][c] = max(dp[v][c], dp[u][c])
    
    print(ans)

if __name__ == "__main__":
    solve()