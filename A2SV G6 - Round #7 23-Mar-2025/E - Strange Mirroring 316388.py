# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

import sys

def input():
    return sys.stdin.readline().strip()

def read_list():
    return list(map(int, input().split()))

def find_char(depth, k, index, original):
    if depth == 1:
        return original[index]
    half_length = 2 ** (depth - 2)
    if k > half_length:
        return find_char(depth - 1, k - half_length, index, original).swapcase()
    return find_char(depth - 1, k, index, original)

def solve():
    original_str = input()
    _ = int(input())
    queries = read_list()
    n = len(original_str)

    results = []
    for k in queries:
        k -= 1
        depth = (k // n) + 1
        index = k % n
        results.append(find_char(61, depth, index, original_str))

    print(*results)

t = int(input())
for _ in range(t):
    solve()