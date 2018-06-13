import random
count = random.randint(1,100)
shu = 0
for i in range(10):
    user = int(input("请输入一个数:"))
    if user > count:
        print("猜大了")
    elif user < count:
        print("猜小了")
    else:
        print("大吉大利，晚上吃鸡")
        break
    shu+=1    
if shu == 1:
    print("大神")
elif shu >1 and shu < 5:
    print("半仙")
elif shu >=5 and shu <9:
    print("休闲")
elif shu >=9 and shu == 10:
    print("蠢材")
           

