#https://leetcode.com/problems/find-the-town-judge/description/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY 


from typing import List


def findJudge(n: int, trust: List[List[int]]) -> int:
    #Check graph notes
    #This is easy graph problem where the relationships are a direct graph (one way link), so not BFS or DFS
    #Need to track the in-degree (number of edges going into a node) and out-degree (number of edges going out of a node)
    #The incoming array will use the indices as the key and the element at the indice as the value (number of edges going in)
    
    #People are label 1 to N (not including zero)
    #Want zeroed lists of length n+1 so you can index 1…n
    incoming = [0]*(n+1)
    outgoing = [0]*(n+1)
    
    for a,b in trust:
        # a trusts b → a has one more outgoing edge, b has one more incoming
        outgoing[a] += 1
        incoming[b] += 1
    
    #scan 1 through n+1 for the judge
    for person in range(1, n+1):
        # judge trusts nobody (outgoing=0)
        # everybody else trusts judge (incoming = n-1)
        if outgoing[person] == 0 and incoming[person] == n-1:
            return person
    
    return -1

trust = [[1,3],[2,3],[3,1]]
result = findJudge(3,trust)
print(result)  