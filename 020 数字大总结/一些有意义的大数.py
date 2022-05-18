""""""

"""

21亿   C语言中的int类型上限 2147483647

77亿   全世界总人口

4000亿  银河系恒星数量

40万亿  人体细胞数量

9e18   C语言longlong上限 9223372万亿  9223372036854775807

3e21   斐波那契数列第100项

1e31   2的100次方  1267650600228229401496703205376

3e38   float类型最大值

10e50 地球上的原子总数

1e80  宇宙中原子总数

1e158  100! 100的阶乘

1e173  围棋的所有可能数

1e208  斐波那契数列第1000项

1.7e308  double类型最大值

"""

fab = [1, 1]
for i in range(1000):
    fab.append(fab[-1] + fab[-2])
print(fab[999])
