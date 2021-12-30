# 两个字符串的删除操作
# dp，自底向上，迭代
def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(n + 1):
        dp[0][i] = i
    for j in range(m + 1):
        dp[j][0] = j
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1]
            else:
                dp[j][i] = min(dp[j - 1][i], dp[j][i - 1]) + 1
    return dp[m][n]


# 带备忘录的递归，自顶向下
def minDistance1(word1, word2):
    # dp(word1, word2, i, j)表示word1[i...n], word2[j...m]的最少删除解
    n = len(word1)
    m = len(word2)
    mem = [[-1 for _ in range(n)] for _ in range(m)]

    def dp(word1, word2, i, j):
        if i == n:
            return m - j
        if j == m:
            return n - i
        if mem[j][i] != -1:
            return mem[j][i]
        else:
            if word1[i] == word2[j]:
                mem[j][i] = dp(word1, word2, i + 1, j + 1)
            else:
                mem[j][i] = min(dp(word1, word2, i + 1, j), dp(word1, word2, i, j + 1)) + 1
            return mem[j][i]

    dp(word1, word2, 0, 0)
    return mem[0][0]


word1 = "seed"
word2 = "seat"
print(minDistance(word1, word2))
print(minDistance1(word1, word2))

