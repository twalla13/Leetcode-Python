#https://leetcode.com/problems/coloring-a-border/description/ 

from typing import List


def colorBorder(grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:

    startingColor = grid[row][col] # 1
    
    rows = len(grid) #3
    cols= len(grid[0]) #3
    visited = set() #Track visited cells in the connected component
    borders = set() #Track cells that are on the border of the connected component

    
    def dfs(i,j):
        if(i,j) in visited:
            return
        visited.add((i,j)) #Mark the cell as visited
        
        is_border = False #assume the cell is not a border cell
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)] #right, left, down, up 
        
        for di, dj in directions: # for each [i,j] go through all the directions
            ni, nj = i + di, j + dj 
            #if the neighbor is out of bounds or a different color, mark as border
            #Check Notes: When a connected cell has at least one neighbor that isn’t part of the component, it indicates that the cell lies at the edge of the region, even if it isn’t on the grid boundary.

            if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] != startingColor:
                is_border = True
            #Otherwise continue DFS if neighbor not yet visited
            elif (ni, nj) not in visited: 
                dfs(ni, nj)
        
        if is_border:
            borders.add((i,j)) #if the current cell is a border add to borders
            
    dfs(row,col)
    
    for i,j in borders:
        grid[i][j] = color #After DFS, only color cells in borders
    
    return grid

result = colorBorder([[1,2,2],[2,3,2]],0,1,3)
print(result) 