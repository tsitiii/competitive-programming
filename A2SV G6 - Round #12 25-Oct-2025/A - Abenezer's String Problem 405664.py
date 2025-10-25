# Problem: A - Abenezer's String Problem - https://codeforces.com/gym/606404/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    max_char = max(s)
    alphabet_size = ord(max_char) - ord('a') + 1
    print(alphabet_size)