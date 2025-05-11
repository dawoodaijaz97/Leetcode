def solve(n: int) -> str:
    def to_base(num: int, base: int) -> str:
        if num == 0:
            return "0"
        digits = []
        while num:
            digits.append(int(num % base))
            num //= base
        return ''.join(str(x) if x < 10 else chr(x - 10 + ord('A')) for x in digits[::-1])
    
    hex_part = to_base(n * n, 16)
    hexatrigesimal_part = to_base(n * n * n, 36)
    
    return hex_part + hexatrigesimal_part