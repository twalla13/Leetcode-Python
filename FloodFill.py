#https://leetcode.com/problems/flood-fill/ 

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    #DFS to find all of the connected nodes in adjancey matrix
    
    row, col= len(image), len(image[0])
    startColor = image[sr][sc] #starting color is a indices sr, sc

    
    if color == startColor: #if the startColor is the same as the color we want to change
        return image

    def dfs(i,j): #recusive DFS search
        if i < 0 or i >= row or j < 0 or j >= col or image[i][j] != startColor:
            return #base case breaks if its out of bounds or not the same color
        image[i][j] = color
        dfs(i-1,j) #top
        dfs(i+1,j) #bottom
        dfs(i,j-1) #left
        dfs(i,j+1) #right
    dfs(sr,sc)
    return image