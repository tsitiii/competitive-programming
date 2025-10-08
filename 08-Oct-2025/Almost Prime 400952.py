# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A


from math import sqrt
n = int(input())
ans = 0

def isPrime(num):
    if num < 2:
        return False
    val = int(sqrt(num))
    for i in range(2, val + 1):
        if num % i == 0:
            return False
    return True


for i in range(3, n + 1):
    cnt = 0
    for j in range(2, i + 1):
        if isPrime(j) and i % j == 0:
            cnt += 1
    if cnt == 2:
        ans += 1
print(ans)