# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        cnt = 0
        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif logs[i] == "../":
                if not stack:
                    continue
                else:
                    cnt -= 1
                    stack.pop()
            else:
                stack.append(logs[i])
                cnt += 1
        return len(stack)
        # print(stack)