# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = []
        for i in range(n):
            people.append(i+1)
        indx = 0
        def winner(indx):
            if len(people) == 1:
                return people[0]
            indx = (indx + (k-1)) % len(people)
            people.pop(indx)
            return winner(indx)
        return winner(indx)
