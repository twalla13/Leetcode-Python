#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4602/

def missingNumber(nums: List[int]) -> int:
    
    #Find min and max
    lo = 0
    hi = len(nums) #we know hi will be the length be n distinct #s in range [0,n]
    
    #create a set of the expected numbers
    expected = set(range(lo, hi +1)) #must be hi+1 to include hi, range goes to one before end value
    
    seen = set(nums)
    
    #Finding the missing element
    #Set subtraction gives you all items in expected that aren’t in seen.
    missing =  expected - seen
    
    #must us pop() bc missing is a set
    #pop() on a set removes and returns arbitrary elements from the set 
    #pop() returns a single number and empties missing
    
    return missing.pop()

result = [3,0,1]
print(missingNumber(result))