"https://leetcode.com/problems/reverse-string/description/ "


def reverseString(s):
    
    
        """
            Fancy Fast way in python
            return " ".join(
                word[::-1]      # Python slice to reverse a string
                for word in s.split()
                )
        """
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        "Strings are arrays"
        
        "MUST BE <= for odd length arrays "
        while(left <= right):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            print(s)
            left += 1
            right -= 1
        
        return s 
        
        
# Call the function and print the result
result = reverseString(["H","a","n","n","a","h"])
print(result) 