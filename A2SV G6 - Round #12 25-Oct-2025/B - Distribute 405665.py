# Problem: B - Distribute - https://codeforces.com/gym/606404/problem/B

n = int(input())
cards = list(map(int, input().split()))
cards_with_indices = [(cards[i], i + 1) for i in range(n)]
cards_with_indices.sort()
target_sum = (sum(cards) * 2) // n

left = 0
right = n - 1
pairs = []

while left < right:
    current_sum = cards_with_indices[left][0] + cards_with_indices[right][0]
    if current_sum == target_sum:
        pairs.append((cards_with_indices[left][1], cards_with_indices[right][1]))
        left += 1
        right -= 1
    elif current_sum < target_sum:
        left += 1
    else:
        right -= 1

for pair in pairs:
    print(pair[0], pair[1])