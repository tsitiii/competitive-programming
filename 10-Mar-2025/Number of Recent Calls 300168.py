# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.recent_count = [] 

    def ping(self, t: int) -> int:
        self.recent_count.append(t)
        while self.recent_count and self.recent_count[0] < t - 3000:
            self.recent_count.pop(0) 
            
        return len(self.recent_count)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)