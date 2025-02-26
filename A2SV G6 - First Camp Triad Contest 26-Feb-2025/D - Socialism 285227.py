# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    savings = list(map(int, input().split()))
    
    savings.sort() 
    total = sum(savings) 
    wealthy = 0  
    for i in range(n):
        remaining = n - i  
        if total / remaining >= x:
            wealthy = remaining
            break
        total -= savings[i]  
    
    print(wealthy)
