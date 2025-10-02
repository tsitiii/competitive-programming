# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
array = []
# memo = {}
for i in range(n):
    arr = list(map(int, input().split()))
    array.append(arr)

dp = [[0]*3 for _ in range(n)]
for j in range(3):
    dp[0][j] = array[0][j]
for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = array[i][j] + max(dp[i-1][j+1], dp[i-1][j+2])
        elif j==1:
            dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j+1])
        elif j == 2:
            dp[i][j] =array[i][j] + max(dp[i-1][j-1], dp[i-1][j-2])
print(max(dp[n-1]))