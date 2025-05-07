# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

n, m = map(int, input().split())

parent = list(range(n + 2))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

output = []

for _ in range(m):
    query = input()
    if query[0] == '?':
        x = int(query[2:])
        res = find(x)
        output.append(str(res) if res <= n else "-1")
    else:
        x = int(query[2:])
        parent[x] = find(x + 1)

print('\n'.join(output))
