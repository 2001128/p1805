import random 
number = random.randint(1,100)
i=0
while i<10:
   # pc = random.randint(1,100)
    py = int(input("请输入您猜的数:"))
    if number < py:
        print("猜大了")
    elif number > py:
        print("猜小了")
    elif number == py:
        print("大吉大利,今晚吃鸡")
        break
    i+=1
    
