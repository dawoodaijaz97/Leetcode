def solve(s: str, t: str) -> int:
    def longest_palindrome_from_single_string(x: str) -> int:
        n = len(x)
        dp = [[0] * n for _ in range(n)]
        max_length = 1
        
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if x[i] == x[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    max_length = max(max_length, dp[i][j])
        
        return max_length
    
    def can_form_palindrome_with_cross(s: str, t: str) -> int:
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    return 2 + longest_palindrome_from_single_string(s[:i]) + longest_palindrome_from_single_string(t[j+1:])
        return 1
    
    max_length = max(
        longest_palindrome_from_single_string(s),
        longest_palindrome_from_single_string(t),
        can_form_palindrome_with_cross(s, t)
    )
    
    return max_length