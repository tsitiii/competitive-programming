# Problem: C - Chain Reaction in the Math Club - https://codeforces.com/gym/606404/problem/C

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    degree[a] += 1
    degree[b] += 1

groups = 0

while True:
    leaves = []
    for i in range(1, n+1):
        if degree[i] == 1:
            leaves.append(i)
    if not leaves:
        break
    for u in leaves:
        degree[u] = -1
        for v in adj[u]:
            if degree[v] > 0:
                degree[v] -= 1
    groups += 1

print(groups)