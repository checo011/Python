# 猜数字游戏
import random

ram_nums = int(random.randint(1, 10))
nums = int(input('请你猜一猜密码是多少吧:'))
while True:
    if nums > ram_nums:
        print('大了')
    if nums < ram_nums:
        print('小了')
    else:
        print('对了')
        exit()