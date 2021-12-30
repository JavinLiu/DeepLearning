# 两个字符串的删除操作

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


word1 = "sea"
word2 = "eat"
print(minDistance(word1, word2))

