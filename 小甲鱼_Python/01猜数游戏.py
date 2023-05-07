# 猜数字游戏
import random

counte = 3
ram_nums = int(random.randint(1, 10))

while counte > 0:
    counte -= 1
    nums = int(input('请你猜一猜密码是多少吧:'))
    if nums > ram_nums:
        print('大了')
    elif nums < ram_nums:
        print('小了')
    else:
        print('对了')
        break
