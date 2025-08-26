#https://leetcode.com/problems/string-to-integer-atoi/description/

def myAtoi(s: str) -> int:
    #ascii function from string to in
            # return X*10
        
        #res = 0

        #if i =0 is "-"
            #flag -1 


        #for i in s:
            #if ascii value of current character in [0,9]
                #res + asciiFun(currentCharacter)
            #else not the number break
                # return result * flag


    
    res = 0
    
    i = 0 
    #must skip the leading spaces to find the flag
    while i < len(s) and s[i] == ' ':
        i += 1
    
    #removed all leading zeros and there is nothing left
    if i == len(s):
        return 0
    
    flag = 1
    #set the flag to negative if after the leading spaces we have '-'
    if s[i] == '-':
        flag = -1
        i += 1
    elif s[i] == '+':
        i += 1 #skip plus sign
    
    
    
    #must handle overflow for when res * 10 + digit exceeds the 32-bit signed range 
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    while i < len(s) and '0' <= s[i] <= '9': #must use the name i index becuase we skipped leading spaces

        digit = ord(s[i]) - ord('0') #ascii of string nums to numeric ints 
        if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
            return INT_MAX if flag == 1 else INT_MIN
 
        # First “4”: res = 0*10 + 4 = 4
	    # Then “2”: res = 4*10 + 2 = 42
        res = (res * 10) + digit
        i += 1
    
    return res * flag

result = myAtoi("   -042")

print(result) 