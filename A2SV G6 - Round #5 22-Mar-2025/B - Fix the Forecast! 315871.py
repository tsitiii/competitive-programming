# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

import sys

def solve():
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))

        a_with_index = sorted((a[i], i) for i in range(n))  # Sort by values of `a`
        b.sort() 
        ans = [0] * n
        for i in range(n):
            _, ind = a_with_index[i]  
            ans[ind] = b[i]  
        
        print(*ans)
solve()
