# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

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