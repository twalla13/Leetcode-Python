# https://leetcode.com/problems/battleships-in-a-board/description/
from ast import List


def countBattleships(board: List[List[str]]) -> int:
    rows, cols = len(board), len(board[0])
    
    visited = set()
    count = 0 
    
    def dfs(i,j, directions: List[tuple]):
        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != "X" or (i,j) in visited:
            return # base case for DFS
        
        #mark cell as seen, want a tuple so we need () around i,j
        visited.add((i,j))

        # 2. shape constraint: 
        #    Only go in one direction per ship.
        #    How will you prevent DFS from turning a corner?
        #    (Hint: record the direction you took from the start.)
        for di, dj in directions:
            dfs(i + di, j + dj, directions)
            
            
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "X" and (r, c) not in visited:
                 # 4. before you DFS, decide if this is the *start* of a ship:
                #    A. no “X” immediately above
                #    B. no “X” immediately to the left
                #    If either is true, this cell is the head of a vertical or horizontal ship.
                #    Otherwise it’s a continuation—skip counting here
                
                
                #ONLY NEED TO CHECK ABOVE AND LEFT FIRST due to going row by row
                #Loop through row on the outter most for loop
                no_above = ( r-1 < 0 or board[r-1][c] != "X")
                no_left = ( c-1 < 0 or board[r][c-1] != "X")
                if not (no_above and no_left):
                    continue #goes to the next value of c in for loop                
                count += 1 #found head of ship
                
                if c + 1 < cols and board[r][c+1] == "X":
                    dfs(r,c, [(0,1)])
                    # →→→  horizontal ship
                    dfs(r, c, [(0, 1)])
                elif r + 1 < rows and board[r + 1][c] == "X":
                    # ↓↓↓  vertical ship
                    dfs(r, c, [(1, 0)])
                else:
                    # single-cell ship
                    visited.add((r, c))
                    # no dfs needed since it has no neighbors

    return count