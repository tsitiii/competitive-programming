# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A


n, target = map(int, input().split())
ans = target // n
if target % n != 0:
    ans +=1
print(ans)

