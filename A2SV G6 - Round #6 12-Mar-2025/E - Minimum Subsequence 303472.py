# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    zeros = []
    ones = []
    group = [0] * n
    cnt = 0
    for i in range(n):
        char = string[i]
        if char == '0':
            if ones:
                group[i] = ones.pop()
            else:
                cnt += 1
                group[i] = cnt
            zeros.append(group[i])
        else:
            if zeros:
                group[i] = zeros.pop()
            else:
                cnt += 1
                group[i] = cnt
            ones.append(group[i])
    print(cnt)
    print(' '.join(map(str, group)))