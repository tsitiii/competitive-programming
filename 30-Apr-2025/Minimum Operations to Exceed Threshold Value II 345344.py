# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = [num for num in nums]
        heapq.heapify(min_heap)
        cnt = 0
        if len(nums) < 2:
            return cnt
        while min_heap[0] < k:
            val1 = heapq.heappop(min_heap)
            val2 = heapq.heappop(min_heap)
            res = (min(val1, val2) *2) + max( val1, val2)
            heapq.heappush(min_heap, res)
            cnt += 1
        return cnt