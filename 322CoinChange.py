# dp[n]表示凑成总金额为n所需的最少硬币数
# x为硬币种类
# dp[n] = min{dp[n - x] + 1, dp[n]}
# 迭代，自底向上
def initDp(n, dp):
    dp.append(0)
    for i in range(1, n + 1):
        dp.append(n + 1)


def coinChange(coins, amount, dp):
    for i in range(amount + 1):
        for x in coins:
            if i - x >= 0:
                dp[i] = min(dp[i - x] + 1, dp[i])
            else:
                continue
    if dp[amount] == amount + 1:
        dp[amount] = -1
    return dp[amount]


coins = [2]
amount = 3
dp = []
initDp(amount, dp)
print(coinChange(coins, amount, dp))


# 暴力求解，递归
def coinChange1(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    else:
        res = amount + 1
        for x in coins:
            subProblem = coinChange1(coins, amount - x)
            if subProblem == -1:
                continue
            res = min(subProblem + 1, res)
        if res == amount + 1:
            return -1
        else:
            return res


print(coinChange1(coins, amount))


# 自顶向下，带备忘录的递归
def coinChange2(coins, amount, dp2):
    if amount == 0:
        return dp2[0]
    if amount < 0:
        return -1
    if dp2[amount] != -2:
        return dp2[amount]
    else:
        res = amount + 1
        for x in coins:
            subProblem = coinChange2(coins, amount - x, dp2)
            if subProblem == -1:
                continue
            res = min(res, subProblem + 1)
        if res == amount + 1:
            return -1
        else:
            return res


dp2 = [-2] * (amount + 1)
# print(dp2)
dp2[0] = 0
# print(dp2)
print(coinChange2(coins, amount, dp2))



