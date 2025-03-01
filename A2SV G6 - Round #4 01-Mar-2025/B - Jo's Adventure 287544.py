# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int,input().split())
building = list(map(int,input().split()))
forsum = [0] * n
forsum[0] = 0
backsum = [0] * n
backsum[n-1] = 0
for i in range(1,n):
    if building[i] < building[i-1]:
        curr  = building[i-1] - building[i]
    else:
        curr = 0
    forsum[i] = curr + forsum[i-1]
for i in range(n-2,-1,-1):
    if building[i] < building[i+1]:
        curr  = building[i+1] - building[i]
    else:
        curr = 0
    backsum[i] = curr + backsum[i+1]
for _ in range(m):
    l, r = list(map(int,input().split()))
    if l > r:
        ans = backsum[r-1] - backsum[l-1] 
        print(ans)
    else:
        ans = forsum[r-1] - forsum[l-1]
        print(ans)
