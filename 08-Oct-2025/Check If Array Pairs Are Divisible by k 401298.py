# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        # fir = arr[0:n//2]
        # sec = arr[n//2:]
        # sec.reverse()
        # # print(firsthalf)
        # # print(secondhalf)
        # flag = True
        # for i in range(n//2):
        #     if (fir[i] + sec[i]) %k != 0:
        #         flag = False
        # return flag
        buckert=[0]*k
        for  n in arr:
            buckert[n%k]+=1
        if k%2==0 and buckert[k//2]%2==1:
            return False
        for i in range(1,k):
            if buckert[i]!=buckert[(-i)%k]:
                return False
        return True