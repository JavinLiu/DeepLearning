# 编辑距离
# dp[i][j]表示s1[0..i]转换为s2[0...j]的编辑距离
# basecase s1为空时:dp[0...i][0]=i;s2为空时:dp[0][0...j]=j
# 状态转移: 插入dp[j][i-1],删除dp[j-1,i],替换dp[j-1,i-1]
# dp[i][j] = min(dp[j][i-1],dp[j-1][i],dp[j-1][i-1])+1
# 最终结果 dp[m][n] m=len(s2),n=len(s1)

# 递归解法
def minDistance1(word1, word2):
    def dp(word1, word2, j, i):
        if i == 0:
            return j
        elif j == 0:
            return i
        else:
            if word1[i - 1] == word2[j - 1]:
                return dp(word1, word2, j - 1, i - 1)
            else:
                return min(dp(word1, word2, j, i - 1), dp(word1, word2, j - 1, i), dp(word1, word2, j - 1, i - 1)) + 1

    return dp(word1, word2, len(word2), len(word1))


# 自顶向下,备忘录的递归，迭代
def minDistance2(word1, word2):
    n = len(word1) + 1
    m = len(word2) + 1
    mem = [[-1 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        mem[0][i] = i
    for j in range(m):
        mem[j][0] = j

    def dp(mem, word1, word2, j, i):
        if mem[j][i] != -1:
            return mem[j][i]
        else:
            if word1[i - 1] == word2[j - 1]:
                mem[j][i] = dp(mem, word1, word2, j - 1, i - 1)
            else:
                mem[j][i] = min(dp(mem, word1, word2, j, i - 1),
                                dp(mem, word1, word2, j - 1, i),
                                dp(mem, word1, word2, j - 1, i - 1)) + 1
            return mem[j][i]
    dp(mem, word1, word2, m - 1, n - 1)
    return mem[m-1][n-1]


# 自底向上解法，迭代，递推
def minDistance(word1: str, word2: str) -> int:
    n = len(word1) + 1
    m = len(word2) + 1
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        dp[0][i] = i
    for j in range(m):
        dp[j][0] = j
    # print(dp)
    for j in range(1, m):
        for i in range(1, n):
            if word1[i - 1] == word2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1]
            else:
                dp[j][i] = min(dp[j][i - 1], dp[j - 1][i], dp[j - 1][i - 1]) + 1
    return dp[m - 1][n - 1]


word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))
print(minDistance1(word1, word2))
print(minDistance2(word1, word2))
