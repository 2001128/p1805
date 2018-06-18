name  = ['李嘉诚','刘强东','雷军']  
print(name [0])  
print(name [1])  
print(name [2])
print(name[0],"有事到不了")  
name[0] = '比尔盖茨'  
  
print(name [0])  
print(name [1])  
print(name [2]) 
print('更大的餐桌')  
name.insert(0,'马云')  
#name.insert(1,'王健林')  
name.insert(name.__len__()//2,'王健林')   
name.append('马化腾')  
for x in name:  
    print('欢迎商业大佬, ',x)  
print("\n只有两个")  
while name.__len__() >2:  
    print('对不起 ' ,name.pop())  
for x in name:  
    print('还在名单上 ',x)  
del name[1]  
del name[0]  
if name.__len__() == 0:  
    print('全空')   
