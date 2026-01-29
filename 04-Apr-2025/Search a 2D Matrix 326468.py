# Problem: Search a 2D Matrix ---https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        n, m = len(matrix), len(matrix[0]) 
        low, high = 0, (n * m) - 1 

        while low <= high:
            mid = (low + high) // 2
            row = mid // m 
            col = mid % m  
            num = matrix[row][col]

            if num == target:
                return True
            elif num < target:
                low = mid + 1  
            else:
                high = mid - 1  

        return False
