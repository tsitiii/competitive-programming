# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(instructions)
        bit = FenwickTree(max_val)
        total_cost = 0
        
        for i, num in enumerate(instructions):
            less = bit.query(num - 1)
            greater = i - bit.query(num)
            total_cost = (total_cost + min(less, greater)) % MOD
            bit.update(num, 1)
        
        return total_cost