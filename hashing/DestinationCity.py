#https://leetcode.com/problems/destination-city/description/

from collections import defaultdict
from typing import List


def destCity(paths: List[List[str]]) -> str:
    #Hash set problem with set difference
    #Create list of the first element of all the sub lists
    
    fromCities = set([path[0] for path in paths])
    toCities = set([path[1] for path in paths])
    
 
    #set difference: which gives you the elements in toCities that are not in fromCities.
    #.pop() removes and returns an arbitrary element from a set

    return (toCities - fromCities).pop()

paths =[["jMgaf WaWA","iinynVdmBz"],
        
        [" QCrEFBcAw","wRPRHznLWS"],
        ["iinynVdmBz","OoLjlLFzjz"],
        ["OoLjlLFzjz"," QCrEFBcAw"],
        ["IhxjNbDeXk","jMgaf WaWA"],
        ["jmuAYy vgz","IhxjNbDeXk"]] #failed this test case
result = destCity(paths)
print(result)