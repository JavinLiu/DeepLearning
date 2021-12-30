# 最小路径和
# 自底向上，迭代
def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


# 带备忘录的迭代，自顶向下
def minPathSum1(grid):
    m = len(grid)
    n = len(grid[0])
    mem = [[-1 for _ in range(n)] for _ in range(m)]

    # dp(i,j)表示从(0,0)-->(i,j)的最小路径和
    def dp(i, j):
        if i == 0:
            res = 0
            for k in range(j + 1):
                res += grid[i][k]
            mem[i][j] = res
            return res
        if j == 0:
            res = 0
            for k in range(i + 1):
                res += grid[k][j]
            mem[i][j] = res
            return res
        if mem[i][j] != -1:
            return mem[i][j]
        else:
            mem[i][j] = min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]
            return mem[i][j]

    return dp(m - 1, n - 1)


def minPathSum2(grid):
    m = len(grid)
    n = len(grid[0])

    def dp(i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return 40000
        return min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]

    return dp(m - 1, n - 1)


def minPathSum3(grid):
    m = len(grid)
    n = len(grid[0])
    mem = [[-1 for _ in range(n)] for _ in range(m)]

    def dp(i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return 40000
        if mem[i][j] != -1:
            return mem[i][j]
        mem[i][j] = min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]
        return mem[i][j]

    return dp(m - 1, n - 1)


# grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
grid = [[1, 2, 3], [4, 5, 6]]
print(minPathSum(grid))
print(minPathSum1(grid))
print(minPathSum2(grid))
print(minPathSum3(grid))
