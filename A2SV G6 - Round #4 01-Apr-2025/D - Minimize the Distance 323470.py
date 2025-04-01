# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
coor = list(map(int, input().split()))
coor.sort()
if n % 2 == 0:
    print(coor[ (n//2) -1])
else:
    print(coor[ ((n+1) // 2) - 1])