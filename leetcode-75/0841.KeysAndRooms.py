class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        toVisit = rooms[0][:]
        while toVisit:
            room = toVisit.pop(0)
            for key in rooms[room]:
                if key not in visited:
                    toVisit.append(key)
            visited.add(room)
        if len(visited) == len(rooms):
            return True
        else:
            return False
