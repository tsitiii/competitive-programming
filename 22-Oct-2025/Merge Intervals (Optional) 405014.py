# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for i in range(len(intervals)):
            start , end = intervals[i]
            if not stack:
                stack.append([start, end])
            else:
                stack_start, stack_end = stack.pop()
                if stack_end >= start:
                    new_start = min(start, stack_start)
                    new_end = max(end, stack_end)
                    stack.append([new_start, new_end])
                else:
                    stack.append([stack_start, stack_end])
                    stack.append([start, end])
        return stack