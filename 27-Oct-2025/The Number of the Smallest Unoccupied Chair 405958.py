# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        friends = [(arrival, leaving, i) for i, (arrival, leaving) in enumerate(times)]
        friends.sort() 
        available_chairs = list(range(n))
        heapq.heapify(available_chairs)
        departures = []
        
        for arrival, leaving, friend_idx in friends:
            while departures and departures[0][0] <= arrival:
                _, chair = heapq.heappop(departures)
                heapq.heappush(available_chairs, chair)
            chair = heapq.heappop(available_chairs)
            
            if friend_idx == targetFriend:
                return chair
            heapq.heappush(departures, (leaving, chair))
        
        return -1