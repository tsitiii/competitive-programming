# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
    
        prev = self.getRow(rowIndex - 1)
        temp = [1]
        for j in range(1 , rowIndex):
            temp.append(prev[j - 1] + prev[j])

        temp.append(1)
        
        return  temp