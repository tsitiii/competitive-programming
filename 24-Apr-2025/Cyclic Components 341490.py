# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from types import GeneratorType
from collections import defaultdict

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if isinstance(to, GeneratorType):
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


from collections import defaultdict
n , m = map(int, input().split())
graph = defaultdict(list)
visited = set()
cycle = False
white = 1
grey = 2
black = 3
flag = True
color ={
    k:white for k in range(1, n+1)
}
cnt = 0

@bootstrap
def dfs(node, parent):
    global flag
    global cnt
    global cycle
    if len(graph[node]) != 2:
        flag = False
    if  cycle or not flag:
        yield
    color[node] = grey
    for ng in graph[node]:
        if color[ng] == white:
            yield dfs(ng, node)
        elif ng != parent and color[ng] == grey:
            cycle = True
            cnt += 1
    color[node] = black
    yield

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    
    if color[i] == white:
        flag = True
        cycle= False
        dfs(i, -1)
        
print(cnt)
# print(color)