# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
n ,  k = map(int,input().split())
message = list(map(int,input().split()))
dq = deque()
seen = set()
for i in range(len(message)):
    if not dq:
        dq.append(message[i])
        seen.add(message[i])
    if message[i] in seen:
        continue
    elif len(dq) >= k:
        rm = dq.popleft()
        seen.remove(rm)
        dq.append(message[i])
        seen.add(message[i])
    else:
        dq.append(message[i])
        seen.add(message[i])
    
print(len(dq))
for i in range(len(dq)-1, -1, -1):
    print(dq[i],end=' ')