# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4611/

# Stack

def makeGood(s: str) -> str:
    stack = []
    
    for c in s:
        print("c:", c)
        
        if stack and str(stack[-1]).casefold() == c.casefold():
            print("stack[-1]:", stack[-1])
            if (c.isupper() and str(stack[-1]).isupper()) or (c.islower() and str(stack[-1]).islower()):
                stack.append(c)
            elif (c.isupper() and str(stack[-1]).islower()) or (c.islower() and str(stack[-1]).isupper()):
                stack.pop()
        else:
            stack.append(c)
        print("stack", stack)
    return "".join(stack)
s = ""
print(makeGood(s))