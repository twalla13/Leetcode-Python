# https://leetcode.com/problems/word-search/description/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows = len(board) 
    cols= len(board[0])
    visited = set() #Track visited cells in the connected component
    def dfs(i,j,idx):
                    #idx is the next index in "word" to match on board
                    
                    if idx == len(word): #Base case for DFS
                        return True
    
                    # 2. out of bounds, revisiting, or wrong letter
                    if (i < 0 or i >= rows or
                        j < 0 or j >= cols or
                        (i, j) in visited or
                        board[i][j] != word[idx]):
                        return False

                    # 3. mark this cell as used
                    visited.add((i, j))

                    # 4. try all 4 directions
                    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                        if dfs(i+di, j+dj, idx+1):
                            return True  # found a path

                    # 5. backtrack so others can use this cell after not finding the path at the current [i,j]
                    visited.remove((i, j))
                    return False
                
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != word[0]:
                continue
            else:
                if dfs(row,col,0):
                    return True
    return False #no path found

strs = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
result = exist(strs,"ABCCED")

print(result)  
