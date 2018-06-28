import random 
computer = random.randint(1,3)
player = int(input("请输入你要出的拳1:石头,2:剪刀,3:布"))
if (player == 1 and computer) or (player == 2 and computer == 3) or (player == 3and computer ==1):
    print("玩家赢")
elif(player == computer):
    print("平局")
else:
    print("电脑赢")

'''
import random
num = random.randint(1,100)
i=0
while True:
    i+=1
    n = int(input("请输入你要猜的数:"))
    if n>num:
        print("猜大了")
    elif n<num:
        print("猜小了")
    else:
        print("恭喜你猜对了")
        break
print("你一共猜了%d次"%i)
if i<=5:
    print("大神啊")
elif i <=10:
    print("还不错哦")
else:
    print("还需要努力哦")
'''
'''
year = int(input("请输入年份:")
if (year %4 == 0) or (year %100 !=0):
    print("闰年")
elif year%400 == 0:
    print("闰年")
else:
    print("平年")
'''
'''
list=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}] 
for i in list:
    for k,v in i.items():
        for j,l in v.items():
            print(k,j,l)
'''
'''
def n_num(num):
    if num == 1:
        return 1
    else:
        return num*n_num(num-1)
result = n_num(5)
print(result)
'''
'''
l = []
for i in range(3):
    x = int(input('',end='\n')) 
    l.append(x) #这里用append()函数，意思是追加元素
    l.sort()
    break
print (l)    
'''
'''
def int(a,b,c):
    l = [a,b,c]
    l.sort()
    return l
x,y,z = int(10,8,6)
print(x,y,z)
'''
'''
l = []
for i in range(3):
    x = int(input('请输入整数:'))
    l.append(x) #这里用append()函数，意思是追加元素
    l.sort()
print (l)
'''
l = []
for i in range(3):
    x = int(input("请输入整数:"))
    l.append(x)
    l.sort()
print(l)

'''    
def a_num(num):
    if num == 1:
        return 1
    else:
        return num *a_num(num-1)
result = a_num(5)
print(result)
'''
