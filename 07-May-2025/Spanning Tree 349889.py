# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # Adjust if 0-indexed
size = [1] * (n + 1)
edges = []

for _ in range(m):
    a, b, w = list(map(int, input().split()))
    edges.append((w, a, b))

edges.sort(key=lambda x: x[0])

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(c, d):
    pu = find(c)
    pv = find(d)
    if pu == pv:
        return False
    if size[pu] > size[pv]:
        parent[pv] = pu
        size[pu] += size[pv]
    else:
        parent[pu] = pv
        size[pv] += size[pu]
    return True

ans = 0
for w, u, v in edges:
    if not union(u, v):
        continue
    ans += w

print(ans)