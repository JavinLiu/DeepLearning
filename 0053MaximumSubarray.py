# dp[i]表示以num[i]为结尾的最大和连续子数组
# i:1-->n j:1-->i - 1
# dp[i] = max{dp[i], dp[i - 1] + num[i]}
# 结果max(dp)

def maxSubArray(nums):
    # 1
    # dp = []
    # n = len(nums)
    # for x in nums:
    #     dp.append(x)
    # print(dp)
    # for i in range(1, n):
    #     dp[i] = max(dp[i], dp[i - 1] + nums[i])
    # print(dp)
    # return max(dp)
    # 2
    # n = len(nums)
    # pre = nums[0]
    # res = max(nums)
    # for i in range(1, n):
    #     cur = max(nums[i], pre + nums[i])
    #     pre = cur
    #     res = max(res, cur)
    # return res
    # 3
    pre = 0
    res = nums[0]
    for x in nums:
        pre = max(x, pre + x)
        res = max(res, pre)
    return res


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
