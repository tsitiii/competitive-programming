# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n, t, c = [int(i) for i in input().split()]
prisoners = [int(i) for i in input().split()]

answer = 0
left = 0
for right in range(n):
    if prisoners[right] > t:
        left = right + 1 
    
    current_length = right - left + 1
    if  current_length >= c:
        answer += 1

print(answer)