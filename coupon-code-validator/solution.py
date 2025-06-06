import re

def solve(code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
    valid_coupons = []
    
    for c, b, a in zip(code, businessLine, isActive):
        if (a and 
            bool(re.match(r'^[a-zA-Z0-9_]+$', c)) and 
            b in {"electronics", "grocery", "pharmacy", "restaurant"}):
            valid_coupons.append((b, c))
    
    valid_coupons.sort(key=lambda x: (["electronics", "grocery", "pharmacy", "restaurant"].index(x[0]), x[1]))
    
    return [c for _, c in valid_coupons]