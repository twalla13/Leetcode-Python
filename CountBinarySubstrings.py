#https://leetcode.com/problems/count-binary-substrings/description/


def countBinarySubstrings(s: str) -> int:

    # s = "0011100"
    # runs = [2 (0’s), 3 (1’s), 2 (0’s)]
    #  adjacent pairs:  [2,3]   and  [3,2]
    #  valid substrings:  
    #    from [2,3] → min=2  ("01", "0011")
    #    from [3,2] → min=2  ("10", "1100")
    #  total = 2+2 = 4
        
    # Track all consecutive group lengths
        groups = [] #length of consecutive runs
        count = 1
        
        # Group consecutive characters
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        
        # Don't forget the last group
        groups.append(count)
        
        # Calculate valid substrings
        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i-1], groups[i])
            
        return result