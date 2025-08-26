#https://leetcode.com/problems/intersection-of-two-arrays-ii/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY

def intersect(nums1, nums2):
    #Sort both arrays
    nums1.sort()
    nums2.sort()
        
    #Loop through both arrays and check:
    #if num1 > num2 then move num2 pointer
    #if num1 < num2 then move num1 pointer
    i , j = 0,0
    toReturn =[]

  # Use 'and' to ensure both pointers are in bounds
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            toReturn.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1  # Increment nums2 pointer
        else:
            i += 1  # Increment nums1 pointer
        
    return toReturn
    
# Call the function and print the result
result = intersect([1, 2, 2, 1], [2, 2])
print(result)  # Output: [2, 2]