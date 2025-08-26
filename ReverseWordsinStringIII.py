#https://leetcode.com/problems/reverse-words-in-a-string-iii/


#Two pointer Example
def reverseWords(s: str) -> str:
    
    list_s = s.split()
    """

        for word in list_s:
        
        that will only change the word variable locally and not inside the list !!!
        That does not change the corresponding entry inside list_s. In Python, iterating over a list gives you a copy of each element (or, if it’s a mutable object, a reference to it), but rebinding the loop variable never writes back to the list.
    """
    for i, word in enumerate(list_s):
        left = 0
        right = len(word) - 1

        # print("left index: ", left)
        # print("right index: ", right)
        #string are immutable in python
        temp_word = list(word)
        while(left <= right):
            temp = temp_word[left]
            temp_word[left] = temp_word[right]
            temp_word[right] = temp
            left += 1
            right -= 1
            # print(temp_word)
            
        # write the reversed word back into list_s
        list_s[i] = ''.join(temp_word)
            
    return " ".join(list_s)


result = reverseWords( "Let's take LeetCode contest")
print(result)