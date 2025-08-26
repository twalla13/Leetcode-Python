#https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/
def areNumbersAscending(s: str) -> bool:
    
    #convert string into list with space as delimeter
    sList = s.split()
    
    prev = 0
    for token in sList:
        if token.isdigit():
            digit = int(token)
            if digit > prev:
                prev = digit
            else:
                return False
    return True

result = areNumbersAscending("1 box has 8 blue 4 red 6 green and 12 yellow marbles")

print(result)