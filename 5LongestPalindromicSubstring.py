# 最长回文字串
# 寻找以s[i]或s[i],s[i+1]为中心的回文串
# i:0...lens(s)-1
#    s1 = s[i]为中心的回文串
#    S2 = s[i],s[i+1]为中心的回文串
#    res = max(res,max(s1,s2))
# 判断回文串
# while left>=0 and right<len(s) and s[left]==s[right]:
#       left--,right++
# return s[left+1,right]


def center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left = left - 1
        right = right + 1
    return s[left + 1: right]


def longestPalindrome(s) -> str:
    n = len(s)
    res = ''
    for i in range(n):
        s1 = center(s, i, i)
        s2 = center(s, i, i+1)
        if len(s1) >= len(s2):
            res = res if len(res) >= len(s1) else s1
        else:
            res = res if len(res) >= len(s2) else s2
    return res


# s = "cbbd"
s = "babad"
print(longestPalindrome(s))
