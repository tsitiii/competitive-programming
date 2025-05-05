# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()

        result = [0] * n
        index_queue = list(range(n))

        for card in deck:
            index = index_queue.pop(0)
            result[index] = card

            if index_queue:
                index_queue.append(index_queue.pop(0))

        return result