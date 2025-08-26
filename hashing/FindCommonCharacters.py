#https://leetcode.com/problems/find-common-characters/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY 

def commonChars(self, words: List[str]) -> List[str]:
    # 1. Pick the shortest word as your candidate list of chars
    base = min(words, key=len)

    result = []
    # 2. For each character in that base word
    for ch in base:
        # 3. Check each other word has at least one of this char
        found_in_all = True
        for w in words:
            if ch not in w:
                found_in_all = False
                break
        if not found_in_all:
            continue  # skip to next char

        # 4. If it exists in every word, we can “use it up” once in each
        result.append(ch)
        #    so it isn’t reused more times than it appears
        for i in range(len(words)):
            # remove only the first occurrence
            words[i] = words[i].replace(ch, "", 1)

    return result