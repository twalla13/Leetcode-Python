#https://leetcode.com/problems/can-place-flowers/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY 

def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        
        # size = len(flowerbed)
        # counter = 0
        # for lpointer in range(size):
        #     rpointer = lpointer + 1  # Right pointer is next index
        #    # print("Left", lpointer , ", right:", rpointer)
        #     if rpointer < size and flowerbed[lpointer] == 0 and flowerbed[rpointer] == 0 : 
        #         rpointer +=1
        #        # print("Next to right", flowerbed[nextRight], " current flowerbed" ,flowerbed)
        #         if flowerbed[nextRight] == 0 or lpointer == 0:
        #             counter += 1
        #     else:
        #         if rpointer == size:
        #             break
    
        
        # if n <= counter:
        #     return True
        # else:
        #     return False
        
        #^^^^ solution above doesnt work because only checks the right neighbor 
        #also it doesnt properly use the counter, not always placing a flower at the correct index so it causes miscounts
        
        
        size = len(flowerbed)
        
        lpointer = 0 
        
        while lpointer < size:
            rpointer = lpointer + 1
            if (flowerbed[lpointer] == 0 and (lpointer == 0 or flowerbed[lpointer - 1] == 0) and (rpointer == size or flowerbed[rpointer]==0)):
                # instead of using a counter, use n to decrement everytime you can place a flower
                n -= 1
                if n == 0: # n is zero and the left pointer is still in bound then we have planted all the possible pots
                    return True #early exist after all flowers are placed

                lpointer += 2 #skip next plot since we cant plant there
            else:
                lpointer += 1
        return n <= 0
        
# Call the function and print the result
result = canPlaceFlowers([1,0,0,0,0,1],2)
print(result) 