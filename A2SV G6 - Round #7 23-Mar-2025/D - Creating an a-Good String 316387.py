# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

def solve(s, l, left, right):
    if left == right:
        return 0 if s[left] == l else 1

    mid = (left + right) // 2

    changes_first_half = 0
    for i in range(left, mid + 1):
        if s[i] != l:
            changes_first_half += 1
    moves_case1 = changes_first_half + solve(s, chr(ord(l) + 1), mid + 1, right)

    changes_second_half = 0
    for i in range(mid + 1, right + 1):
        if s[i] != l:
            changes_second_half += 1
    moves_case2 = changes_second_half + solve(s, chr(ord(l) + 1), left, mid)

    return min(moves_case1, moves_case2)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(s, 'a', 0, n - 1))