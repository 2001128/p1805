'''
i=0
while i<10:
    print("hello")
    i+=1
'''
'''
day = int(input("请输入年份:"))
if day % 4 == 0 and day %100 !=0:
    print("闰年")
elif day % 400 ==0:
    print("闰年")
else:
    print("平年")
'''
'''
i = 1
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,j*i),end="\t")
    print("")
    i+=1
'''


i = 0
for i in range(10):
    j=1
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,j*i),end="\t")
    print("")
    i+=1



















