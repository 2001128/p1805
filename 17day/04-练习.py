
'''
for i in range(10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,j*i),end="\t")
    print("")
'''

'''
import random
n = random.randint(1,100)
#print("生成随机数%d"%n)
i=0
while True:
    num = int(input("请输入你要猜的数字:"))
    i+=1
    if (num>n):
        print("猜大了")
    elif(num<n):
        print("猜小了")
    else:
        print("恭喜你答对了")
        break
print("一共猜了%d次"%i)
if i<=5:
    print("你太聪明了!")
elif i<=10:
    print("还可以，下次努力")
else:
    print("你猜的方法有待改进!")
'''

'''
year = int(input("请输入年份:"))
if year%4 == 0 and year%100 != 0:
    print("今年是闰年")
elif year%400 == 0:
    print("今年是闰年")
else:
    print("今年是平年")
'''

'''
import random
i = 0
while i<=10:
    i+=1 
    computer = random.randint(1,3)
    player = int(input("1:请输入要出的拳:1:石头,2:剪刀,3:布"))
    if computer > 0 and computer < 4:
        if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
            print("玩家赢")
        elif player == computer:
            print("平局")
        else:
            print("电脑赢")
        
    else:
        print("输入格式有误")
'''

'''
list=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]
for i in list:
    for k,v in i.items():
        for j,l in v.items():
            print(k,j,l)
'''

'''
def c_num(num):
    if num == 1:
        return 1
    else:
        return num*c_num(num-1)
result = c_num(5)
print(result)
'''

'''
stus = [{"name":"zhangsan", "age":18},{"name":"lisi", "age":19},{"name":"wangwu", "age":17}]
stus.sort(key = lambda x:x['name'])
stus.sort(key = lambda x:x['age'])
print(stus)
'''



