#https://leetcode.com/problems/excel-sheet-column-title/description/

def convertToTitle(columnNumber: int) -> str:
        #Based 26 but A doesnt start at zero s00
        #Its based 26 plus 1
        
        ans = []
        
        # mapping = {} #key - > alphabet
        # alphabet = list('abcdefghijklmnopqrstuvwxyz')
        # num = 0
        # for a in alphabet:
        #     mapping[num] = a
        #     num +=1
        
        # build a 0→'A', 1→'B', … map
        mapping = {i: chr(ord('A') + i) for i in range(26)}
        #print(mapping)
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            #print(remainder)
            ans.append(mapping[remainder])
            
            # columnNumber = int(columnNumber / 26)
            # move to next “digit”
            columnNumber //= 26
            
        #built from least significant to most, so reverse
        ans.reverse()
        return "".join(ans)
    
result = convertToTitle(28)

print(result) 