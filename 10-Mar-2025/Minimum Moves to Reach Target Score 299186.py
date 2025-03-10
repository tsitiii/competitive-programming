# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt  = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 == 0:
                target //=2
                maxDoubles -= 1
            else:
                target -= 1
            cnt += 1
        cnt += (target -1)
        return cnt