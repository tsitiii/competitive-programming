# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 1:
            return [[1]]
        else:
            res.append([1])
            for i in range(1, numRows):
                prev = res[-1]
                new_row = [1]
                for j in range(1,i):
                    an = prev[j] + prev[j-1]
                    new_row.append(an)
                new_row.append(1)
                res.append(new_row)
        return res
