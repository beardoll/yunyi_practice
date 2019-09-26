# coding=utf8
# 待排序数组
a = [5, 3, 1, 4, 2]
# 存储最终结果
b = []
#[0, 1, 2, 3, 4]
for i in range(5):
    # min_v: 当前数组a的最小值
    # min_p: 当前数组a最小值在a中的位置
    min_v = 10000
    min_p = -1
    # pos: 指示x在数组a中的位置
    pos = 0
    for x in a:
        if x < min_v:
            # 如果找到了新的最小值，更新min_v和min_p
            min_v = x
            min_p = pos
        # 每访问a中的一个元素，pos加一，以指示a的下一个元素
        pos += 1
    # 将当前最小值存入b中
    b.append(min_v)
    # 删除a中的最小值
    a[min_p] = []

print(b)
