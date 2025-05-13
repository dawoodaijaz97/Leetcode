def solve(numWays: list[int]) -> list[int]:
    n = len(numWays)
    denominations = []

    for i in range(1, n):
        if numWays[i] == 0:
            continue

        # Check if the current amount can be formed with existing denominations
        possible = False
        for d in denominations:
            if (i - d) >= 0 and numWays[i - d] > 0:
                possible = True
                break

        if not possible:
            return []

        # If it's the first valid amount, add it as a denomination
        if i == 1 or numWays[i - 1] == 0:
            denominations.append(i)

    return sorted(denominations)