# LIFO Insight:
# This solution uses a stack (Last-In-First-Out) because when navigating file paths,
# directories are added in order, but a ".." undoes the most recent (last) addition.
# Recognizing this undo-last behavior is a key signal to use a stack.

def simplifyPath(path: str) -> str:
    
    parts = path.split('/')
    
    # Initialize an empty list to act as a stack (LIFO structure).
    stack = []
    # Iterate through each part split by '/' to process meaningful directory names.
    for c in parts:
        # Skip empty strings and current directory references ('.') since they don’t change the path.
        if c == "" or c == ".":
            continue
        # '..' means go up one directory, so pop the top of the stack if it's not empty.
        elif c == "..":
            if stack: 
                stack.pop()
        # Valid directory name – push onto the stack (LIFO) to track the path hierarchy.
        else:
            stack.append(c)
    # Join the stack with '/' to form the final simplified path. Prepend '/' for absolute path.
    if stack:
        return "/" + "/".join(stack)
    else:
        return "/"
        
    
    # stack = []
    # i = 0

    
    # while i < len(path):
        
    #     if path[i] == '/':
    #         if stack and stack[-1] == '/' and i == len(path) - 1: #route directory
    #             stack.pop()
    #             return "".join(stack)
    #         elif stack and stack[-1] == '/': #dont want to add duplicate slashes 
    #             i += 1 #not adding them to stack
    #         else:
    #             stack.append(path[i])
    #             i += 1
    #     elif path[i] == ".":
    #         counter = 0 
    #         temp = i
    #         while temp < len(path) and path[temp] == ".": 
    #             counter += 1
    #             temp += 1
    #         if stack and counter <= 2:
    #             stack.pop() #removes starting 
    #             i += 1
    #         else:
    #             while i < len(path) and path[i] == '.': #will this move the c in path as well?? 
    #                 stack.append(path[i])
    #                 i += 1
    #     else:
    #         stack.append(path[i])
    #         i += 1
            
    # res = "".join(stack)
    # # Remove trailing slash unless it's root
    # if len(res) > 1 and res[-1] == '/':
    #     res = res[:-1]
    return res
path = "/.../a/../b/c/../d/./"
print(simplifyPath(path))