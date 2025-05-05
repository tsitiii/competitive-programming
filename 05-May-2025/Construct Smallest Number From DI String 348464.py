# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        num = [0] * (n + 1)
        available_digits = list(range(1, n + 2))  

        def find_smallest(index):
            if index == n + 1:
                return True  

            for digit in available_digits[:]:
                if index > 0:
                    if pattern[index - 1] == 'I' and num[index - 1] >= digit:
                        continue 
                    if pattern[index - 1] == 'D' and num[index - 1] <= digit:
                        continue  
                num[index] = digit
                available_digits.remove(digit)  

                if find_smallest(index + 1):
                    return True  
                num[index] = 0
                available_digits.append(digit)
                available_digits.sort() 

            return False

        find_smallest(0)
        return "".join(map(str, num))  