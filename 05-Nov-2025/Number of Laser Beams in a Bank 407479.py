# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        total = 0
        
        for row in bank:
            devices = row.count('1')
            if devices > 0:
                total += prev * devices
                prev = devices
                
        return total