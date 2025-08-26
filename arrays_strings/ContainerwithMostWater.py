from typing import List
#https://leetcode.com/problems/container-with-most-water/ 

def maxArea(height: List[int]) -> int:
    
    #Max amount of water = area
    #Area = length * width
    
    #left = i+1, and right= len(height)
    #length = min of left and right pointers
    #width = right - left

    #use the left and right pointers to go through the list until left > right
    #while looping track the max area
    

    left = 0
    right = len(height) - 1
    maxArea=0
    
    while left < right:
        
        length = min(height[left], height[right])
        width = right - left
        
        
        tempArea = length * width
        print("length ", length, ", width", width, ", current area", tempArea)
        if maxArea < tempArea:
            maxArea = tempArea
            
        #only want to move the pointer that has the smaller height 
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxArea
        

# Call the function and print the result
result = maxArea([1,8,6,2,5,4,8,3,7])
print(result) 