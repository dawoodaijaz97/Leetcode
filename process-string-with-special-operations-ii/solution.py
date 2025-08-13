def solve(s: str, k: int) -> str:
    result = []
    
    for char in s:
        if char.isalpha():
            result.append(char)
        elif char == '*':
            if result:
                result.pop()
        elif char == '#':
            result.extend(result)
        elif char == '%':
            result.reverse()
    
    final_result = ''.join(result)
    
    return final_result[k] if 0 <= k < len(final_result) else '.'