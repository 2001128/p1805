for i in range(1,6):#打印多少行
    for j in range(0,6-i):#打印空格
        print(" ",end= "")#打印空格
    for k in range(1,i):#打印*
        print("* ",end= "")
    print(" ")#换行
