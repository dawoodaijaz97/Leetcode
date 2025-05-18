def solve(s: str, t: str) -> int:
    def longest_palindrome_substring(s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_length = 0

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 1 or length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    max_length = length

        return max_length

    # Check for palindromes in s and t individually
    max_palindrome_s = longest_palindrome_substring(s)
    max_palindrome_t = longest_palindrome_substring(t)

    # Check for palindromes formed by concatenating a substring from s and a substring from t
    max_cross_palindrome = 0
    for i in range(len(s)):
        for j in range(len(t) - 1, -1, -1):
            if s[i] == t[j]:
                # Find the longest palindromic prefix in s[:i+1]
                left_palindrome_length = longest_palindrome_substring(s[:i + 1])
                # Find the longest palindromic suffix in t[j:]
                right_palindrome_length = longest_palindrome_substring(t[j:])
                max_cross_palindrome = max(max_cross_palindrome, left_palindrome_length + right_palindrome_length)

    return max(max_palindrome_s, max_palindrome_t, max_cross_palindrome)