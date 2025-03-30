# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers):
        answer_count = Counter(answers)
        total_rabbits = 0
        
        for answer, count in answer_count.items():
            groups = ceil(count / (answer + 1))
            total_rabbits += groups * (answer + 1)
        
        return total_rabbits