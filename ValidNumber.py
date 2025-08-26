#https://leetcode.com/problems/valid-number/

def isNumber(s: str) -> bool:
    
    # Rules for valid number:
    #     optional sign -> first nonspace char can be -,+ but only once
    #     digits and decimal -> can have digits 0-9 and only ONE . before the exponent
    #     digits after decimal -> must be at least one digit on either side of . (cannot have .)
    #     optional exponent -> represented as e or E and must be followed by optional sign and at least one digit, only one exponent per number, only digits after exponent
    #     NO MULTIPLE DECIMALS OR SIGNS (--2 OR 1.2.3)
    
    
    # How to think about loops and checks -> FLAGS:
    #     Track different states with flags
        
    #     -> Have you seen a sign?
    #         if so then if its seen again its not a valid number 
    #     -> Have you seen a digit yet? 
    #         if not then . might be invalid unless at least one digit
    #     -> Have you seen a decimal yet?
    #         cannot have multple decimals so use a flag 
    #     -> Have seen a exponent yet?
    #         after we seen an exponent switch to an exponent mode 
    #     -> Have we started reading after exponent?
    #         because an exponent must be followed by at least one digit (optional sign first)
    
    
    i = 0
    
    saw_digit = False
    saw_decimal = False
    saw_Exponent = False
    exponentMode = False
    
    if s[i] == '-':
        i += 1
    elif s[i] == '+':
        i += 1
    
    while i < len(s):
        if s[i].isdigit():
            saw_digit = True
            i += 1
        elif s[i] == '.' and not saw_Exponent and not saw_decimal:
            saw_decimal = True
            i += 1
        elif (s[i] == 'e' or s[i] == 'E') and not saw_Exponent and saw_digit:
            saw_Exponent = True
            
            #RESET the saw_digit because now we are in exponent mode for exponent digits
            saw_digit = False
            i += 1
            
            #check for optional sign again 
            if i < len(s) and  s[i] == '-':
                i += 1
            elif  i < len(s) and   s[i] == '+':
                i += 1
        else:
            return False
    
    return saw_digit

result = isNumber(".")

print(result)