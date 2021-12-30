# 无重叠区间
# 贪心：按活动时间end排序, 遍历1->n个活动，如果start<end，则区间重叠，活动冲突;反之，区间不重叠，活动不冲突，更新end
def eraseOverlapIntervals(intervals):
    # sort_inter = sorted(intervals, key=lambda x: [x[1], x[0]])
    intervals = sorted(intervals, key=lambda x: x[1])
    # pre = intervals[0]
    pre = intervals[0][1]
    res = 0
    for i in range(1, len(intervals)):
        # if intervals[i][0] < pre[1]:
        if intervals[i][0] < pre:
            res += 1
        else:
            pre = intervals[i][1]
    return res


# intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# intervals = [[1, 2], [1, 2], [1, 2]]
intervals = [[1, 2], [2, 3]]
print(eraseOverlapIntervals(intervals))
