#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4667/

# Monotonic

class StockSpanner:

    def __init__(self):
        self.stack = [] #stack that keeps track of the min prices


    def next(self, price: int) -> int:
        span = 1
    
        while self.stack and self.stack[-1][0] <= price:
            # self.stack.pop()
            # span += self.stack[-1][1] -> unsafe
            
            #You’re trying to access self.stack[-1][1] after you’ve popped the top element, which may leave the stack empty and lead to wrong span accumulation (or even an error in edge cases).
            
            #You want to pop first, then accumulate that popped span, like this:
            popPrice, popSpan = self.stack.pop()
            span += popSpan
            
        self.stack.append((price, span))
        print(self.stack)
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)åprint(self.stack)