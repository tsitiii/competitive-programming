# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dq = deque()
    for num in arr:
        if not dq:
            dq.append(num)
        elif num < dq[0]:
            dq.appendleft(num)
        else:
            dq.append(num)
    print(*dq)