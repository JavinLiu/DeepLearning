# 最长公共子序列
# dp解，自顶向下，迭代
def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
            else:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
    return dp[m][n]


# 带备忘录的递归，第底向上
def longestCommonSubsequence1(text1, text2):
    # dp(text1, text2, i, j)表示text1[i...n]与text2[j...m]的最长公共子序列
    # mem[i, j]用于存放dp(text1, text2, i, j)的值，初始值为-1，表示当前dp未计算
    n = len(text1)
    m = len(text2)
    mem = [[-1 for _ in range(n)] for _ in range(m)]
    # for i in range(n):
    #     mem[m][i] = 0
    # for j in range(m):
    #     mem[j][n] = 0

    def dp(text1, text2, i, j):
        if i == n or j == m:
            return 0
        if mem[j][i] != -1:
            return mem[j][i]
        else:
            if text1[i] == text2[j]:
                mem[j][i] = dp(text1, text2, i + 1, j + 1) + 1
                return mem[j][i]
            else:
                mem[j][i] = max(dp(text1, text2, i + 1, j), dp(text1, text2, i, j + 1))
                return mem[j][i]
    dp(text1, text2, 0, 0)
    return mem[0][0]


text1 = "abcde"
text2 = "ace"
# text1 = "abc"
# text2 = "abc"
# text1 = "abc"
# text2 = "def"
print(longestCommonSubsequence(text1, text2))
print(longestCommonSubsequence1(text1, text2))
