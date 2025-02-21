# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import defaultdict
t = int(input())
for _ in range(t):
        n, k, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        left, result = 0, k + 1
        shows = defaultdict(int)
        for right in range(len(arr)):
            shows[arr[right]] += 1
            if right - left + 1 == d:
                result = min(result, len(shows))
                shows[arr[left]] -= 1
                if shows [arr[left]] == 0:
                    shows.pop(arr[left])
                left += 1
        print(result)