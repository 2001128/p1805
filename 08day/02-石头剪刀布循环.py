'''
两个人玩的游戏
电脑玩家
普通玩家
1代表石头
2代表剪刀
3代表布
'''
import random#导入随机工具 只导入一次
i=0#作为while条件
while i<10:
    pc = random.randint(1,3)#每次随机生成一个数字大小是1-3之间
    py = int(input("请输入1:石头2:剪刀3:布"))#用户输入的
#下面判定谁赢谁输
    if py > 0 and py < 4:
        if  (py==1 and pc==2) or (py==2 and pc==3) or (py==3 and pc==1):
            print("玩家赢了")
        elif py==pc:
            print("平局")
        else:
            print("电脑赢了")
    else:
        print("输入有误")
    i+=1
