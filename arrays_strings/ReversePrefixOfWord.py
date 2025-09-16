#https://leetcode.com/problems/reverse-prefix-of-word/description/?envType=problem-list-v2&envId=ajc81mgt 
# Sliding Window Dynamic 


def reversePrefix(word: str, ch: str) -> str:
    
    #Sliding window w/ Dynamic Window size
    #Valid subarry
    word = list(word)
    left = 0
    for right in range(len(word)):
        if word[right] == ch :
            while (left <= right):
                temp = word[left]
                word[left] = word[right]
                word[right] = temp
                left += 1
                right -= 1
            #must return here bc its the first occurrence of ch 
            return "".join(word)
        else:
            right += 1
            
    return "".join(word)
word = "abcdefd"
ch = "d"
print(reversePrefix(word, ch))