# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = {}

if n == 1:
    print(0)
else:
    dp[0] = 0
    for i in range(1,n):
        mincost = float('inf')
        for j in range(1, k+1):
            if i-j>=0:
                cost = dp[i-j] + abs(arr[i] - arr[i-j])
                mincost = min(cost, mincost)
        dp[i] = mincost
print(dp[n-1])