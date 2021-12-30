# 俄罗斯套娃信封问题

# 贪心解，错了
# 不能先考虑按宽递增再考虑按高递增
# 二者是不分先后的
# 如高和宽都满足装入条件时，但一个宽小高大，一个高小宽大，此时选择更小的高还是更小的宽是不能确定的
# def maxEnvelopes1(envelopes) -> int:
#     sort_env = sorted(envelopes, key=lambda x: [x[0], x[1]])
#     print(sort_env)
#     n = len(envelopes)
#     count = 1
#     pre = sort_env[0]
#     max_h = pre[1]  # 当前最大高度
#     for i in range(1, n):
#         cur = sort_env[i]
#         # 宽相同，选高小的
#         if cur[0] == pre[0]:  # 宽相同
#             if pre[1] > cur[1] > max_h:  # 选高小的,但要比当前最大高度大
#                 pre = sort_env[i]
#         # 宽大高大, 信封+1
#         if cur[0] > pre[0] and cur[1] > pre[1]:
#             count += 1
#             pre = sort_env[i]
#             max_h = pre[1]
#     return count


# dp解
# dp[n]表示以envelopes[n]为结尾时的最多信封个数
# base case: dp[0] = 1, 只有一个信封的时候
# 状态转移:
# i:1->n-1; j:0->i;
# dp[i] = max(符合条件的dp[j] + 1)
# 结果：max(dp)
def maxEnvelopes(envelopes) -> int:
    sort_env = sorted(envelopes, key=lambda x: [x[0], -x[1]])
    n = len(sort_env)
    # print(sort_env)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sort_env[i][1] > sort_env[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def maxEnvelopes1(envelopes):
    sort_env = sorted(envelopes, key=lambda x: [x[0], x[1]])
    n = len(sort_env)
    # print(sort_env)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sort_env[i][0] > sort_env[j][0] and sort_env[i][1] > sort_env[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
# envelopes = [[1,1],[1,1],[1,1]]
# envelopes = [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]
# envelopes = [[10,8],[1,12],[6,15],[2,18]]
print(maxEnvelopes(envelopes))
print(maxEnvelopes1(envelopes))
