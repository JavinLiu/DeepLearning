# 两个字符串的最小ASCII删除和
# dp自底向上，迭代
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


# 自顶向下，带备忘录的递归
def minimumDeleteSum1(s1, s2):
    # dp(s1, s2, i, j)表示s1[i...n],s2[j...m]的最小删除和，存储在mem[i][j]中
    n = len(s1)
    m = len(s2)
    mem = [[-1 for _ in range(n)] for _ in range(m)]

    def dp(s1, s2, i, j):
        if i == n:
            res = 0
            for k in range(j, m):
                res += ord(s2[k])
            return res
        if j == m:
            res = 0
            for k in range(i, n):
                res += ord(s1[k])
            return res
        if mem[j][i] != -1:
            return mem[j][i]
        else:
            if s1[i] == s2[j]:
                mem[j][i] = dp(s1, s2, i + 1, j + 1)
            else:
                mem[j][i] = min(dp(s1, s2, i + 1, j) + ord(s1[i]), dp(s1, s2, i, j + 1) + ord(s2[j]))
            return mem[j][i]
    dp(s1, s2, 0, 0)
    return mem[0][0]


s1 = "delete"
s2 = "leet"
print(minimumDeleteSum(s1, s2))
print(minimumDeleteSum1(s1, s2))
