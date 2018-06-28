#第一种方法:
l = [1,100,49,10,56,3,2,37]
i = 0
while i < len(l):
    if l[i] == 3:
        print("索引是:%d"%i)
        break
    i+=1
#第二种方法:
position = l.index(3)
print("索引是:%d"%position)

#第三种方法:
for position,i in enumerate(l):
    if i == 3:
        print("索引是:%d"%position)
        break
#第四种方法:
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] >l[j]:
            l[i],l[j] = l[j],l[i]
        print(l)

min = 0
max = len(l) -1
count = 3
while True:
    center = int((min+max)/2)
    if l[center] > count:
        max = center -1
    elif l[center] < count:
        min = center+1
    elif l[center] == count:
        print("索引是%d"%center)
        break
