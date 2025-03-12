# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

n = int(input())
string =  input()
stack = []
for  char in string:
    if stack and char != stack[-1]:
        stack.pop()
    else:
        stack.append(char)
print(len(stack))