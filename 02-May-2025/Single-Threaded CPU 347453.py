# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
        sorted_tasks.sort()
        
        min_heap = [] 
        result = []
        current_time = 0
        i = 0  
        
        while i < len(tasks) or min_heap:
            while i < len(tasks) and sorted_tasks[i][0] <= current_time:
                heappush(min_heap, (sorted_tasks[i][1], sorted_tasks[i][2])) 
                i += 1
            if min_heap:
                process_time, idx = heappop(min_heap)
                result.append(idx)
                current_time += process_time
            else:

                if i < len(tasks):
                    current_time = sorted_tasks[i][0]
        
        return result
    