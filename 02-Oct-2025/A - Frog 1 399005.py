# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

m = int(input())
arr = list(map(int, input().split()))
memo = [0] * m
if m == 1:
    print(0)
else:
    memo[0] = 0
    memo[1] = abs(arr[1] - arr[0])
    
    for i in range(2, m):
        cost1 = memo[i-1] + abs(arr[i] - arr[i-1])
        cost2 = memo[i-2] + abs(arr[i] - arr[i-2])
        
        memo[i] = min(cost1, cost2)

print(memo[m-1])