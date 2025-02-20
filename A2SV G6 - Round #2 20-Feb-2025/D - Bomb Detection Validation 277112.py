# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n, m = map(int, input().split())
bomb = [input().strip() for _ in range(n)]  
directions = [
    (-1, 0), (0, -1), (-1, -1),
    (1, 0), (0, 1), (1, 1),
    (1, -1), (-1, 1)
]

def inbound(i, j):
    return 0 <= i < len(bomb) and 0 <= j < len(bomb[0])

valid_field = True 

for i in range(len(bomb)):
    for j in range(len(bomb[0])):
        if bomb[i][j].isdigit():
            num = int(bomb[i][j])
            bomb_count = 0
            for row, col in directions:
                ni, nj = i + row, j + col
                if inbound(ni, nj) and bomb[ni][nj] == '*':
                    bomb_count += 1
            if bomb_count != num:
                valid_field = False
                break  
        elif bomb[i][j] == '.':
            for row, col in directions:
                ni, nj = i + row, j + col
                if inbound(ni, nj) and bomb[ni][nj] == '*':
                    valid_field = False
                    break 
            
    if not valid_field:
        break  

if valid_field:
    print("YES")
else:
    print("NO")