def solve(s: str) -> str:
    stack = []
    
    for char in s:
        if stack and (ord(char) == ord(stack[-1]) + 1 or 
                      ord(char) == ord(stack[-1]) - 1 or 
                      (stack[-1] == 'a' and char == 'z') or 
                      (stack[-1] == 'z' and char == 'a')):
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)