def solve(words: list[str]) -> list[int]:
    def longest_common_prefix(a: str, b: str) -> int:
        min_length = min(len(a), len(b))
        for i in range(min_length):
            if a[i] != b[i]:
                return i
        return min_length

    n = len(words)
    answer = [0] * n

    # Precompute the longest common prefix lengths between adjacent pairs
    lcp = [[0] * (n - 1) for _ in range(n)]
    for i in range(n - 1):
        lcp[i][i + 1] = longest_common_prefix(words[i], words[i + 1])
        if i > 0:
            lcp[i][i - 1] = longest_common_prefix(words[i], words[i - 1])

    # Calculate the answer for each index
    for i in range(n):
        max_lcp = 0
        if i > 0:
            max_lcp = max(max_lcp, lcp[i - 1][i])
        if i < n - 1:
            max_lcp = max(max_lcp, lcp[i][i + 1])
        answer[i] = max_lcp

    return answer