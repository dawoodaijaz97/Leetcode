def solve(n: int) -> list[int]:
    components = []
    power_of_ten = 1
    
    while n > 0:
        digit = (n // power_of_ten) % 10
        if digit != 0:
            components.append(digit * power_of_ten)
        power_of_ten *= 10
    
    return sorted(components, reverse=True)