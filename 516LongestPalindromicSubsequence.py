# 最长回文子序列
# dp[i][j]表示s[i...j]中的最长回文子序列长度
# 最终结果则在dp[0][n-1]处
# 状态转移，求dp[p][q]:
#       if s[p]==s[q]: dp[p][q]=dp[p+1][q-1]+2
#       else: dp[p][q] = max(dp[p+1][q],dp[p][q-1])

def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n-1]


s = "bbbab"
print(longestPalindromeSubseq(s))






