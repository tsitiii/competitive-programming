# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import defaultdict
k = int(input())
s = input()
dic = defaultdict(int)
prefix = 0
cnt = 0
dic[0] = 1
for num in s:
    prefix += int(num)
    res = prefix-k
    cnt += dic[res]
    dic[prefix] +=1
print(cnt)