# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

t = int(input())
word = input()
result = ""
i = 1
index = 0 
while index < t:
    result += word[index]
    i += 1
    index += i
print(result)
