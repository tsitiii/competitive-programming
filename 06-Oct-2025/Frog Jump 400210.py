# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or stones[0] != 0:
            return False
        stone_set = set(stones)
        target = stones[-1]
        memo = {}
        def dfs(stone, k):
            if stone == target:
                return True
            if (stone, k) in memo:
                return memo[(stone, k)]
            for next_jump in [k - 1, k, k + 1]:
                if next_jump > 0:
                    next_stone = stone + next_jump
                    if next_stone in stone_set:
                        if dfs(next_stone, next_jump):
                            memo[(stone, k)] = True
                            return True
            memo[(stone, k)] = False
            return False
        return dfs(0, 0)




