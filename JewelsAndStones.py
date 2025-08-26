#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4664/

from collections import Counter


def numJewelsInStones(jewels: str, stones: str) -> int:
    stonesCount = Counter(stones)
    ans = 0
    for j in jewels:
        if j in stonesCount:
            ans += stonesCount[j]
    return ans



jewels = "aA"
stones = "aAAbbbb"
result = numJewelsInStones(jewels, stones)
print(result)