# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x^ y
        an =  bin(ans)
        res =Counter(an)
        fin = 0
        print(res)
        for val in res:
            if val == '1':
                fin = int(res[val])
                
        return fin
        