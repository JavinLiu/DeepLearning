# 下降路径最小和
# dp[n][n] 表示从第一行任一个元素到第n行第n个元素的下降路径最小和
# dp[0][0...n-1] = matrix[0][0...n-1]
# dp[n][n] = min(dp[n-1][n-1],dp[n-1][n],dp[n-1][n+1]) + matrix[n][n]
# res = max(dp[n])
def minFallingPathSum(matrix):
    n = len(matrix)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[0][i] = matrix[0][i]
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
            elif j == n - 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + matrix[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
    # print(dp)
    return min(dp[n - 1])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(minFallingPathSum(matrix))
