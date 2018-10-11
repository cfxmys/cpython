"""--- 第一个小游戏 ---"""
temp = input("猜一下小甲鱼现在心里想的哪个数字")
guess = int(temp)
if guess == 8:
    print("你是小甲鱼心里的蛔虫吗")
    print("就是才中了也没有奖励，哈哈")

else:
    if guess < 8:
        print("哈哈，猜小了~~")
    else:
        print("嘿嘿，猜大了~~")

print("游戏结束了，不玩了")
