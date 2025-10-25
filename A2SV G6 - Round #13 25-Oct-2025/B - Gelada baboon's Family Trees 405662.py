# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/607625/problem/B

from collections import defaultdict
from types import GeneratorType

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


n = int(input())
parents = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(1, n + 1):
    graph[i].append(parents[i-1])
    graph[parents[i-1]].append(i)
visited = set()
cnt = 0
@bootstrap
def dfs(node):
    visited.add(node)
    for ng in graph[node]:
        if ng not in visited:
            yield dfs(ng)
    yield
    
for i in range(1, n + 1):
    if i not in visited:
        cnt += 1
        dfs(i)

print(cnt)

