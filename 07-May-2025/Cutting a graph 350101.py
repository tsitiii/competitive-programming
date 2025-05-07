# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

class Disjoint:
    def __init__(self, n):
        self.parent = [ i for i in range(n+1)]
        self.size = [1]*(n+1)
        
    def union(self, a,b):
        pa = self.find(a)
        pb = self.find(b)
        if self.size[pa] > self.size[pb]:
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.parent[pa] = pb
            self.size[pb] += self.size[pa]
            
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    def ask(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        return pu == pv
        
n, m,k = list(map(int, input().split()))
manager = Disjoint(n)
edges = []
operations = []
for _ in range(m):
    src, dest = map(int, input().split())
    edges.append((src,dest))
    
for _ in range(k):
    arr = list(map(str, input().split()))
    operations.append(arr)
ans = []
for i in range(len(operations)-1, -1, -1):
    op, u , v = operations[i]
    if op == "ask":
        if manager.ask(int(u), int(v)):
            ans.append("YES")
        else:
            ans.append("NO")
    else:
        manager.union(int(u), int(v))
for i in range(len(ans)-1, -1,-1):
    print(ans[i])