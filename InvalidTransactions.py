# https://leetcode.com/problems/invalid-transactions/description/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY

from collections import defaultdict
from typing import List

def invalidTransactions(transactions: List[str]) -> List[str]:
    
    #Grouping similar to mapping, almost like a table
    groups = defaultdict(list)
    
    #track invalid transaction in the list
    invalidFlag = invalidFlag = [False] * len(transactions)
    i = 0
    
    while i < len(transactions):
        name, time_str, amount_str, city = transactions[i].split(",")
        time = int(time_str)
        amount = int(amount_str)
        
        if amount > 1000:
            invalidFlag[i] = True
        if name in groups:
            for prev_time, prev_city, prev_idx in groups[name]:
                
                if abs(prev_time - time) <= 60 and city != prev_city:
                    invalidFlag[i] = True #track current idx
                    invalidFlag[prev_idx] = True #track the prev idx
                    
        #append current transaction
        groups[name].append((time, city, i))
        i += 1
    
    res = []
    i = 0
    while i < len(transactions):
        
        if invalidFlag[i] == True:
            res.append(transactions[i])
        i += 1
            
            
    return res
    

transactions = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
result = invalidTransactions(transactions)
print(result)