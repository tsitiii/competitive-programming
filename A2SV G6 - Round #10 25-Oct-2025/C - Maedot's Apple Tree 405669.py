# Problem: C - Maedot's Apple Tree - https://codeforces.com/gym/602812/problem/C

import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        graph = [[] for _ in range(n+1)]
        for __ in range(n-1):
            u = int(data[idx]); idx += 1
            v = int(data[idx]); idx += 1
            graph[u].append(v)
            graph[v].append(u)
        
        leaf_count = [0]*(n+1)

        parent = [-1]*(n+1)
        stack = [(1, -1, 0)]
        # order = []
        while stack:
            u, p, st = stack.pop()
            if st == 0:
                parent[u] = p
                stack.append((u, p, 1))
                for v in graph[u]:
                    if v != p:
                        stack.append((v, u, 0))
            else:
                if len(graph[u]) == 1 and u != 1:  # leaf
                    leaf_count[u] = 1
                else:
                    total = 0
                    for v in graph[u]:
                        if v != parent[u]:
                            total += leaf_count[v]
                    leaf_count[u] = total
        
        q = int(data[idx]); idx += 1
        for __ in range(q):
            x = int(data[idx]); idx += 1
            y = int(data[idx]); idx += 1
            results.append(str(leaf_count[x] * leaf_count[y]))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()