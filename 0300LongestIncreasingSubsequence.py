# dp[n]表示以num[n]结尾的最长递增子序列长度
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))
