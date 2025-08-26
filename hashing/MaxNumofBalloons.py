#https://www.youtube.com/watch?v=fVCBqMHwhww&ab_channel=GregHogg

from collections import Counter, defaultdict

def maxNumberOfBalloons(text):
        """
        :type text: strPer
        :rtype: int
        """
        letterCounts= Counter(text)
        

        max_b = letterCounts['b']
        max_a = letterCounts['a']
        max_n = letterCounts['n']
        
        #interger division will tell us min 
        #If you only have 3 ‘l’s, 3 // 2 == 1, so you can only make one balloon before you’d need a third ‘l’.
        
        #Modulo (%) tells you “what’s the leftover after you take away as many pairs of l’s as you can.”
        #Integer division (//) tells you “how many full pairs of l’s you have.”
        max_l = letterCounts['l'] // 2
        max_o = letterCounts['o'] // 2
        
        #whichever letter we run out of first determines limit
        return min(max_b, max_a, max_l, max_o, max_n)
        # #That pattern (count → divide by needed qty → min) is the standard for “how many times can I build this multiset out of these supplies.”
        # counter = defaultdict(int)
        # balloon = 'balloon'
        
        # for c in text: #loop through each char in string
        #     if c in balloon: #check if the character is in the string ballon
        #         counter[c] += 1 #if that char key didnt exist in dictionary(map) then gives default value of type (int) == 0 
        
        # #any function in python will check for each character in balloon string in the counter dictionary
        # if any(c not in counter for c in balloon): #any of the balloon char are not in the counter dictionary then no ballons
        #     return 0
        # else:
        #     #return the min of b,a, n, l/2 so that we have 2 l's (int division) and same for 2 o's o/2
        #     return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])
        
