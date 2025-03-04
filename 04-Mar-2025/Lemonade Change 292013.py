# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {}
        for bill  in bills:
            if bill in dic:
                dic[bill] += 1
            else:
                dic[bill] = 1
            if bill == 5:
                continue
            elif bill == 10:
                if dic.get(5,0) > 0:
                    dic[5] -= 1
                else:
                    return False
            elif bill == 20:
                if dic.get(10,0) > 0 and dic.get(5,0) >0:
                    dic[10] -= 1
                    dic[5] -= 1
                elif dic.get(5,0) >=3:
                    dic[5] -= 3
                else:
                    return False
        return True