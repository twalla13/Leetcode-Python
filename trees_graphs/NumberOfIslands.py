#https://leetcode.com/problems/number-of-islands/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY

from typing import List


def numIslands(grid: List[List[str]]) -> int:
    row, col = len(grid), len(grid[0])
    visited = set()
    count = 0 
    def dfs(i,j):
        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != "1" or (i,j) in visited:
            return # base case for DFS
        
        #mark cell as seen, want a tuple so we need () around i,j
        visited.add((i,j))
        
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            dfs(i + di, j + dj)
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                count += 1
                
    return count

grid = [["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
result = numIslands(grid)

print(result)  