#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4606/


from collections import Counter, defaultdict
from typing import List


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    #Create a map: Player # -> Wins
    playersWins = defaultdict(int)
    
    ans = [[], []]
    
    #Kinda like set subtraction 
    losers = {l for _, l in matches}
    winners = {w for w, _ in matches}
    ans[0] = list(winners - losers)
    
    #Counter will build a dict like object with Player -> Frequency Count Of Player
    #loss_counts[player] == # of loses for that player
    
    
    loss_counts = Counter(loser for _, loser in matches)
    
    #filter for frequency of 1 
    #to access loss_counts items like a iterable need to use .items()
    for player, count in loss_counts.items():
        if count == 1:
            ans[1].append(player)
    
    ans[0].sort()
    ans[1].sort()
    return ans

#Doesnt work because not looking for average of wins and losses
    # for match in matches:
    #     #Increment value for player if its in win column
    #     playersWins[match[0]] += 1
        
    #     #Decrement value for player if its in win column
    #     playersWins[match[1]] -= 1
    # for player in playersWins:
    #     if playersWins[player] > 0:
    #         #add to the ans[0] column
    
    #         ans[0].append(player)
    #     if playersWins[player] == 0:
    #         #add to ans[1] colum
    #         ans[1].append(player)
    # return ans
        
    
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(findWinners(matches))