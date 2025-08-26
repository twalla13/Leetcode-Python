# https://leetcode.com/problems/walls-and-gates/description/

from collections import deque
from typing import List


def wallsAndGates(rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rows, cols = len(rooms), len(rooms[0])
        visited = set()
        queue = deque()
        
        
        #First need to queue up all the gates
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c)) #stops from visiting cells twice
        
        distance = 0 #since we are starting a gates distance is zero
        while queue: #go through the queue and preform BFS on each one
            
            #go through all positions in queue
            for i in range(len(queue)):
                r,c = queue.popleft() #deque from front of queue 
            
                rooms[r][c] = distance
                
                #Need to add every neighbor to visited list and the queue
                for di, dj in [[0,1], [1,0],[0,-1], [-1,0]]:
                    ni, nj = r + di, c + dj
                    
                    
                    #if neighbor cell is out of bounds or equal to a wall (-1)
                    if ni < 0 or ni >= rows or nj < 0 or nj >= cols or  (ni,nj) in visited or rooms[ni][nj] == -1:
                        continue 
                    visited.add((ni,nj))
                    queue.append((ni,nj))
            distance += 1
        
        return rooms


rooms =  [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
result = wallsAndGates(rooms)

print(result)  