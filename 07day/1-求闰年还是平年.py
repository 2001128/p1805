'''
year=int(input("请输入年:"))
if year % 4 == 0 and year % 100 != 0:
    print("闰年")
elif year % 400 == 0:
    print("闰年")
else:
    print("平年")
'''





'''
year=int(input("请输入有多少天:"))
if year %4 ==0 and year % 100!=0: 
    print("闰年")
elif year %400 ==0:
    print("闰年")
else:
    print("平年")
'''

i = 1
while i<10:
    j=1
    while j<i:
        print("*",end="")
        j+=1
    print("")
    i+=1
           
