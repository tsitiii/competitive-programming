# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

from collections import deque
n,x = map(int, input().split())
dq = deque()
children =[]
distress = 0
for _ in range(n):
    string = input()
    children.append(string)
for char  in children:
    if '+' in char:
        a,b = char.split()
        x += int(b)
    elif '-' in char:
        a,b = char.split()
        if x >= int(b):
            x-= int(b) 
        else:
            distress += 1
print(x, distress)

