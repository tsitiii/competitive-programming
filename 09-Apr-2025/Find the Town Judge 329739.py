# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] *(n+1)
        outdegree = [0]*(n+1)
        # outdegree = defaultdict(int)
        for a, b in trust :
            outdegree[a] += 1
            indegree[b] += 1    
        ans = -1
        for i in range(len(outdegree)):
            if indegree[i] == n-1 and outdegree[i] == 0 and i!=0:
                ans = i
        return ans
