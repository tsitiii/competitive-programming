# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

left ,right = 0, 0
length = 0
sum1 = sum2 = 0
while left < n and right < m:
    sum1 += arr1[left]
    sum2 += arr2[right]
    
    if sum1 == sum2:
        length += 1
        left += 1
        right += 1
    elif sum1 < sum2:
        sum2 -= arr2[right]
        left += 1
    else:
        sum1 -= arr1[left]
        right += 1
        
if sum1 == sum2  and left == n and right == m:
    print(length)
else:
    print(-1)