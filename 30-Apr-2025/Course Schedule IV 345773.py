# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        order = []
        for i in range(len(prerequisites)):
            fir, sec = prerequisites[i]
            graph[fir].append(sec)
            incoming[sec] += 1
        que = deque()
        for i in range(len(incoming)):
            if incoming[i] == 0:
                que.append(i)
        ans = []
        previous = defaultdict(set)
        while que:
            for i in range(len(que)):
                node = que.popleft()
                for ng in graph[node]:
                    incoming[ng] -= 1
                    if incoming[ng] == 0:
                        que.append(ng)
                    previous[ng].update(previous[node])
                    previous[ng].add(node)
                    
        for u, v in queries:
            if u in previous[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        
        
        
        # for u, v in queries:
        #     if v in graph[u]:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        # return ans

        

        