" https://leetcode.com/problems/squares-of-a-sorted-array/description/ "
def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        "initialize arrays with default-value*length "
        
        toReturn = [0]* len(nums) 
        
        #Due to sorted input array we will start at opposite ends of array
        #Largest negative and largest positive will be at opposite ends
        lpointer = 0 
        rpointer = len(nums) - 1
        i=1
        
        #must be less than or equal to so that the result array fills in index zero
        while lpointer <= rpointer:
            if abs(nums[lpointer]) > abs(nums[rpointer]):
                toReturn[len(nums)-i] = nums[lpointer]**2
                lpointer += 1
                i += 1
            else:
                toReturn[len(nums)-i] = nums[rpointer]**2
                "MUST DECREMENT RIGHT POINTER "
                rpointer -= 1
                i += 1
        
        return toReturn

# Call the function and print the result
result = sortedSquares([-7,-3,2,3,11])
print(result)  