# Problem: A - Can I Get Your Number ? - https://codeforces.com/gym/607625/problem/A

from collections import defaultdict
n = int(input())
string = []
for _ in range(n):
    phone = input()
    num = list(phone)
    string.append(phone)

ans = string[0]

for i in range(1,n):
    k=0
    temp =''
    while k <len(ans) and ans[k]==string[i][k]:
        temp += ans[k]
        k += 1
    ans = temp
print(len(ans))
