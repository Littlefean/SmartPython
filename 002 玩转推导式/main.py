# a = [dog for dog in range(100)]
a = list(range(100))

# 如果列表是一个等差数列，直接用range更快了

b = [i + 1 for i in range(100)]
b_ = list(range(1, 101))

c = [i for i in range(100) if i % 2 == 0]
c_ = list(range(0, 100, 2))
