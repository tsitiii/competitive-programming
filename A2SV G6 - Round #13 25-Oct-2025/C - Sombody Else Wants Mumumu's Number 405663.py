# Problem: C - Sombody Else Wants Mumumu's Number - https://codeforces.com/gym/607625/problem/C

from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = Counter(arr)
    maxf = max(freq.values())
    
    if maxf > n - maxf:
        print(2 * maxf - n)
    else:
        print(n % 2)