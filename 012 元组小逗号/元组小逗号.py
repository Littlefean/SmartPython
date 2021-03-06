print([[[[[[[[[]]]]]]]]])  # [[[[[[[[[]]]]]]]]] 没问题
# print({{{{{{}}}}}})  # 集合不可以嵌套

print(bool((())))  # False
print(bool(((),)))  # True  不要小看这个小逗号，对解析非常有影响
print(bool(((((((((((((()))))))))))))))  # False
print(bool((((((((((((((),))))))))))))))  # True

# 加不加小逗号
print(())
print((()))  # 二层元组
print(((((((((((())))))))))))  # 多层元组，如果里面没有东西还是会解析成一层
print(() == (((((()))))))  # True
print(id(()), id((((())))))  # id 也是一样的

# 如何加小逗号
print(())
print((()))
print(((),))
print("=====4维元组====")
t1 = (((())))
t2 = ((((),)))  # 相同的，都是二维元组
t3 = (((()),))  # 相同的，都是二维元组
t4 = (((())),)  # 相同的，都是二维元组
t5 = ((((),),))
t6 = ((((),),),)

print(t1, t2, t3, t4, t5, t6)

a = 1
b = (1)
print(a, b)  # 一样的

# 过程，从外往里看，如果小括号里面只有一个东西，就忽略这个多余的小括号。

# 总结：加小逗号可以防止被解释器忽略

tup1 = (1, 2)
tup2 = tup1
tup1 += (1,)
print(tup1, tup2)