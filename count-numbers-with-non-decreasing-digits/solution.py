MOD = 10**9 + 7

def count_non_decreasing(base: int, length: int) -> int:
    dp = [[0] * (base + 1) for _ in range(length + 1)]
    dp[0][0] = 1
    
    for i in range(1, length + 1):
        for j in range(base + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
                dp[i][j] %= MOD
    
    return sum(dp[length]) % MOD

def count_up_to(s: str, base: int) -> int:
    length = len(s)
    total = 0
    for i in range(1, length):
        total += count_non_decreasing(base, i)
        total %= MOD
    
    dp = [[0] * (base + 1) for _ in range(length + 1)]
    dp[0][0] = 1
    
    for i in range(length):
        digit = int(s[i], base)
        for j in range(digit + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
        if digit > 0:
            total += sum(dp[i + 1])
            total %= MOD
    
    return total

def solve(l: str, r: str, b: int) -> int:
    count_l = count_up_to(l, b)
    count_r = count_up_to(r, b)
    count_l_minus_1 = count_up_to(str(int(l, b) - 1), b)
    
    return (count_r - count_l_minus_1 + MOD) % MOD