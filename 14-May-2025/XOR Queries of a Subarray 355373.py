# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        prefix = [0] * (len(arr)+1)
        for i in range(1, len(arr)+1):
            prefix[i] = prefix[i-1]  ^ arr[i-1]
        print(prefix)
        for left, right in queries:
            res = prefix[right +1] ^ prefix[left] 
            ans.append(res)
        return ans