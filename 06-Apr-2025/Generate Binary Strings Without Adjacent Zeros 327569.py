# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def recursion(result, remain):
            if remain == 0:
                ans.append(''.join(result))
                return
            if not result or result[-1] == '1':
                result.append('0')
                recursion(result, remain - 1) 
                result.pop()

            result.append('1')
            recursion(result, remain - 1) 
            result.pop()
        
        recursion([], n)
        return ans

           
                
                
                    