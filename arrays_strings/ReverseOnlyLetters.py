#https://leetcode.com/problems/reverse-only-letters/submissions/1751752733/?envType=problem-list-v2&envId=ajc81mgt
# String

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        #Two pointers with left and right at oppsite ends 
        #strings are not immutable in python make it a list
        s = list(s)
        left = 0 
        right = len(s) - 1

        while left <= right:
            if s[right].isalpha() and s[left].isalpha():
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
            else:
                if s[right].isalpha():
                    left += 1
                else:
                    right -= 1
        return "".join(s) #join the list back together