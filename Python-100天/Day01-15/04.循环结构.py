# 1.九九乘法表

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         # i是第一个数字；j是第二个数字
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()
'''

结果如下：

# 1*1=1
# 2*1=2   2*2=4
# 3*1=3   3*2=6   3*3=9
# 4*1=4   4*2=8   4*3=12  4*4=16
# 5*1=5   5*2=10  5*3=15  5*4=20  5*5=25
# 6*1=6   6*2=12  6*3=18  6*4=24  6*5=30  6*6=36
# 7*1=7   7*2=14  7*3=21  7*4=28  7*5=35  7*6=42  7*7=49
# 8*1=8   8*2=16  8*3=24  8*4=32  8*5=40  8*6=48  8*7=56  8*8=64
# 9*1=9   9*2=18  9*3=27  9*4=36  9*5=45  9*6=54  9*7=63  9*8=72  9*9=81

# '''

# 2.判断是不是素数

# from math import sqrt

# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

# row = int(input('请输入行数: '))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()
