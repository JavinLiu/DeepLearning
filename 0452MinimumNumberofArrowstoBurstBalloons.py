# 用最少数量的箭引爆气球
# 贪心: 按气球end坐标排序, 遍历1->n个气球，如果start<=end，则区间重叠，可以一件穿透;反之，区间不重叠，需要一根新箭，同时更新end
def findMinArrowShots(points):
    points = sorted(points, key=lambda x: x[1])
    pre = points[0][1]
    res = 1
    for i in range(1, len(points)):
        if points[i][0] <= pre:
            continue
        else:
            pre = points[i][1]
            res += 1
    return res


# points = [[10, 16], [2, 8], [1, 6], [7, 12]]
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(findMinArrowShots(points))
