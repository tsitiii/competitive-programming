# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        que = deque([0])
        while que:
            curr = que.popleft()
            if curr not in visited:
                visited.add(curr)
                for room in rooms[curr]:
                    if room not in visited:
                        que.append(room)
        return len(visited) == len(rooms)
        

