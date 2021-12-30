# 两个字符串的最小ASCII删除和
def minimumDeleteSum(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, n + 1):
        dp[0][i] = dp[0][i - 1] + ord(s1[i - 1])
    for j in range(1, m + 1):
        dp[j][0] = dp[j - 1][0] + ord(s2[j - 1])
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1]
            else:
                dp[j][i] = min(dp[j - 1][i] + ord(s2[j - 1]), dp[j][i - 1] + ord(s1[i - 1]))
    return dp[m][n]


s1 = "delete"
s2 = "leet"
print(minimumDeleteSum(s1, s2))
