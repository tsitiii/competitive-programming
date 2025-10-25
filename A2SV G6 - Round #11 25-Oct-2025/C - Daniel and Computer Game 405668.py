# Problem: C - Daniel and Computer Game - https://codeforces.com/gym/604781/problem/C

from collections import deque

def solve():
    n, k = map(int, input().split())
    left = input().strip()
    right = input().strip()
    walls = [left, right]
    
    visited = [[False] * (n + 10) for _ in range(2)]
    
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = True
    
    while queue:
        side, h, time = queue.popleft()
        nh = h + 1
        if nh >= n:
            print("YES")
            return
        if nh > time and not visited[side][nh] and walls[side][nh] != 'X':
            visited[side][nh] = True
            queue.append((side, nh, time + 1))
        nh = h - 1
        if nh >= 0 and nh > time and not visited[side][nh] and walls[side][nh] != 'X':
            visited[side][nh] = True
            queue.append((side, nh, time + 1))
        
        nh = h + k
        if nh >= n:
            print("YES")
            return
        other_side = 1 - side
        if nh > time and not visited[other_side][nh] and walls[other_side][nh] != 'X':
            visited[other_side][nh] = True
            queue.append((other_side, nh, time + 1))
    
    print("NO")

if __name__ == "__main__":
    solve()