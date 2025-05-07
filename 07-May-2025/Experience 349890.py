# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
        self.points = [0] * (n + 1)

    def find(self, x):
        # if self.parent[x] == x:
        #     return x
        # self.parent[x] = self.find(self.parent[x])
        # return self.parent[x]
        while x!= self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.size[pa] > self.size[pb]:
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]
            self.points[pb] -= self.points[pa]
        else:
            self.parent[pa] = pb
            self.size[pb] += self.size[pa]
            self.points[pa] -= self.points[pb]

    def add(self, a, b):
        root = self.find(a)
        self.points[root] += b
    
    def get(self, x):
        ans = self.points[x]
        while x != self.parent[x]:
            x = self.parent[x]
            ans += self.points[x]
        return ans

n, m = map(int, input().split())
manager = DisjointSet(n)

for _ in range(m):
    arr = list(map(str, input().split()))
    
    if arr[0] == "join":
        u, v = int(arr[1]), int(arr[2])
        manager.union(u, v)
    elif arr[0] == "add":
        u, v = int(arr[1]), int(arr[2])
        manager.add(u, v)
    elif arr[0] == "get":
        val = int(arr[1])
        print(manager.get(val))