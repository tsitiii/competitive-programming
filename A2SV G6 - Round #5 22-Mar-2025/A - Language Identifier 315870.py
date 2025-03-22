# Problem: A - Language Identifier - https://codeforces.com/gym/591928/problem/A

t = int(input())
for _ in range(t):
    s = input()
    if s[-1] == 'o':
        print("FILIPINO")
    elif s[-1] == 'u':
        print("JAPANESE")
    elif s[-1] == 'a':
        print( "KOREAN")