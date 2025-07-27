def solve(n: int) -> int:
    def is_special(num: int) -> bool:
        num_str = str(num)
        if num_str != num_str[::-1]:
            return False
        digit_count = {}
        for digit in num_str:
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1
        for digit, count in digit_count.items():
            if int(digit) != count:
                return False
        return True

    n += 1
    while not is_special(n):
        n += 1
    return n