from machine import Pin
import time

# 创建行的对象
row1 = Pin(16, Pin.OUT)
row2 = Pin(17, Pin.OUT)
row3 = Pin(18, Pin.OUT)
row4 = Pin(19, Pin.OUT)
row_list = [row1, row2, row3, row4]  # 将创建的行对象放到list里面

# 创建列的对象
col1 = Pin(20, Pin.IN, Pin.PULL_DOWN)
col2 = Pin(21, Pin.IN, Pin.PULL_DOWN)
col3 = Pin(22, Pin.IN, Pin.PULL_DOWN)
col4 = Pin(26, Pin.IN, Pin.PULL_DOWN)
col_list = [col1, col2, col3, col4]  # 将创建的列对象放到list里面

# 键盘矩阵表，后面用来判断按下的是哪个按钮
names = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

# 关于enumerate的作用大家请看https://blog.csdn.net/fanfangyu/article/details/124595937
while True:
    # enumerate多用于在for循环中得到计数，利用它可以同时获得索引和值，即需要index和value值的时候可以使用enumerate
    for i, row in enumerate(row_list):  # 遍历序号和对应的值 # 目的：只让某一行通电，其他的行都是0
        for temp in row_list:  # 遍历行对象
            temp.value(0)  # 给每一个行对象赋值
        row.value(1)
        time.sleep_ms(10)  # 键盘通电后，延迟一小会
        for j, col in enumerate(col_list):  # 遍历序号和对应的值
            if col.value() == 1:  # 给每一个列对象赋值
                print("按键: {} 被按下".format(names[i][j]))
        # print(row1.value(), row2.value(), row3.value(), row4.value())  # 打印出每行的值
        # print(col1.value(), col2.value(), col3.value(), col4.value())  # 打印出每列的值
        # print("-" * 30)

    time.sleep(0.1)
