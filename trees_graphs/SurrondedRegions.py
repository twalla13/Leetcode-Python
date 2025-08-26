#https://leetcode.com/problems/surrounded-regions/ 


from typing import List


def solve(board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        def dfs(i,j): #recusive DFS search
             if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != "O":
                return 
                board[i][j] = "E"
                dfs(i + 1, j) #down 
                dfs(i - 1, j) #up
                dfs(i, j + 1) #right
                dfs(i, j - 1) #left
     
     
        #find the  row edges and label them as E
        for i in range(row):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][col-1] == "O":
                dfs(i, col -1)
        #find the  col edges and label them as E
        for j in range(col):
            if board[0][j] == "O":
                dfs(0,j)
            if board[row - 1][j] == "O":
                dfs(row-1, j)
        
        #flip remaining O to X and change E to O
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"
# Call the function and print the result
result = solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
print(result) 