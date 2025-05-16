def solve(s: str) -> str:
    stack = []
    for char in s:
        if stack and (ord(char) == ord(stack[-1]) + 1 or 
                      ord(char) == ord(stack[-1]) - 25 or 
                      ord(stack[-1]) == ord(char) + 1 or 
                      ord(stack[-1]) == ord(char) - 25):
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)