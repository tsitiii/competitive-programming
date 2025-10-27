# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        target_bits = num2.bit_count()
        
        x = 0
        remaining_bits = target_bits
        for i in range(31, -1, -1):
            bit_mask = 1 << i
            if num1 & bit_mask and remaining_bits > 0:
                x |= bit_mask
                remaining_bits -= 1
        for i in range(32):
            bit_mask = 1 << i
            if remaining_bits > 0 and not (x & bit_mask):
                x |= bit_mask
                remaining_bits -= 1
        
        return x