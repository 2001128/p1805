#添加10个不重复的数
import random
list = []
a=0
while len(list)<10:
    b=random.randint(1,100)
    list.append(b)
    c = list[a]
    a+=1
    if list.count(c)>1:
        list.pop()
        a+=1
print(list)






