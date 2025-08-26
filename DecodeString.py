#https://leetcode.com/problems/decode-string/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY

from collections import deque


def decodeString(s: str) -> str:
    stk = deque()
    buildCount = 0
    current_string = ""
    res = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            #capture multi digit numbers
            temp = ""
            while i < len(s) and s[i].isdigit():
                temp += s[i] 
                i += 1
            buildCount = int(temp)
        elif s[i] == '[':
            #open bracket then push tuple current_string and build count
            stk.append((current_string, buildCount))
            
            #rest current string and buildCount
            current_string = ""
            buildCount = 0
            i += 1
            
        elif s[i] == ']':
            # pop the last (string_so_far, repeat_count)
            prev_string, repeat_count = stk.pop()
            
            
            # now you can rebuild: repeat the current_string repeat_count times
            # and append it back to whatever was in prev_string
            current_string = prev_string + current_string * repeat_count
            i += 1
        else: #current character is a char add to current string and move on
            current_string += s[i]
            i += 1
            
            
            
    return current_string


result = decodeString("3[a2[c]]")
print(result)