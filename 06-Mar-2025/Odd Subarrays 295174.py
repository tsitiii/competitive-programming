# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = i = 0
    while i < n:
        if i+1 < n and arr[i] > arr[i+1]:
            cnt += 1
            i += 2
        else:
            i += 1
    print(cnt)