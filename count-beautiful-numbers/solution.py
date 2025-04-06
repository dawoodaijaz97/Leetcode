def solve(l: int, r: int) -> int:
    def is_beautiful(num: int) -> bool:
        digits = [int(d) for d in str(num)]
        product = 1
        total_sum = 0
        for digit in digits:
            product *= digit
            total_sum += digit
        return product % total_sum == 0

    count = 0
    for num in range(l, r + 1):
        if is_beautiful(num):
            count += 1
    return count