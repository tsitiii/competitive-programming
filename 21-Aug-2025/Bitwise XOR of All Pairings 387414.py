# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        for m in nums1:
            xor1 ^= m
        xor2 = 0
        for n in nums2:
            xor2 ^= n
        return (xor1 if len(nums2) % 2 == 1 else 0) ^ (xor2 if len(nums1) % 2 == 1 else 0)