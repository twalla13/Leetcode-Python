# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY

def strStr(haystack: str, needle: str) -> int:

    #Sliding window better time complexity
    # lengths of haystack and needle
    # n, m = len(haystack), len(needle)
    # # edge case: empty needle always matches at 0
    # if m == 0:
    #     return 0

    # # slide a window of size m over haystack
    # # range(n - m + 1) ensures the window stays in bounds
    # for i in range(n - m + 1):
    #     # haystack[i:i+m] is a slice from i up to (but not including) i+m
    #     # Python slice syntax: string[start:end]
    #     if haystack[i : i + m] == needle:
    #         return i  # first full match

    # return -1  # no match found


    #Two pointer approach, O(n^2) 
    
    if len(haystack) < len(needle):
        return -1
    
    # track current start index
    first_index = -1
    hay = 0
    while hay < len(haystack):
        if haystack[hay] == needle[0]:
            #potential match start index
            first_index = hay
            
            #cycle through characters in needle 
            #BUT do this with a separate pointer
            j = hay
            for n in needle:
                
                #check bounds before comparing
                if j < len(haystack) and haystack[j] == n: #character exists in haystack and needle
                    j += 1
                else: # mismatch, break and start again
                    break
            else: #for ... else loop runs the else block if the for loop never breaks
                return first_index
            
            #if the for loop broke early, reset hay to next possible start
            hay = first_index + 1
            continue #jump back to while loop
        else: #no match on first char of needle, move on
            hay += 1
    return -1


result = strStr("badnotsad", "sad")

print(result)  