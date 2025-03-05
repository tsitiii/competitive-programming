# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
           while stack and temperatures[i]> temperatures[stack[-1]]:
                index=stack.pop()
                answer[index]=i - index
           stack.append(i  )
        return answer
        