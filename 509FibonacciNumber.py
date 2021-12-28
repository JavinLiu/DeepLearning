# 递归解
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# 带备忘录的递归 自顶向下
def initDp(n, dp):
    dp.append(0)
    dp.append(1)
    for i in range(2, n + 1):
        dp.append(-1)


def fib1(n, dp):
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib1(n-1, dp) + fib1(n-2, dp)
        return dp[n]


# 迭代，自底向上，递推
def fib2(n, dp):
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]


# 优化后的迭代
def fib3(n):
    cur = 0
    pre = 1
    if n == 0 or n == 1:
        return n
    else:
        for i in range(2, n + 1):
            temp = pre
            pre = cur + pre
            cur = temp
    return pre


dp1 = []
dp2 = []
x = 10
print(fib(x))

initDp(x, dp1)
fib2(x, dp1)
print(dp1[x])

initDp(x, dp2)
fib2(x, dp2)
print(dp2[x])

print(fib3(x))


