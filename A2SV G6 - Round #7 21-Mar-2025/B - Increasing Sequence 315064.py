# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if i == 0:
            if a[i] == 1:
                b.append(2)
            else:
                b.append(1)
        else:
            ans = b[i-1] + 1
            if ans == a[i]:
                ans += 1
            b.append(ans)
    
    print(b[-1])