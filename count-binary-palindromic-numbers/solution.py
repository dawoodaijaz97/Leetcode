def solve(n: int) -> int:
    def is_palindrome(x: str) -> bool:
        return x == x[::-1]

    count = 0
    for i in range(n + 1):
        if is_palindrome(bin(i)[2:]):
            count += 1
    return count