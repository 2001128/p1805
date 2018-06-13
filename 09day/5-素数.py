##除了1和其本身，其他都不能整除  
'''
i=1  
j=1  
for i in range(2,101):  
    for j in range(2,i):  
        if i%j==0:  
            break;  
        elif (i-1)==j:  
            print ('素数有:%d'%(i)) 
'''
for i in range(2,101):
    flag = 10
    for j in range(2,i):
        if i%j == 0:
            flag = 0
            break
    if flag == 10:
        print("2~100之间素数有:%d"%i) 
