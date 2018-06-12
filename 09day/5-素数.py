##除了1和其本身，其他都不能整除  
i=2  
j=2  
for i in range(2,101):  
    for j in range(2,i):  
        if i%j==0:  
            break;  
        elif (i-1)==j:  
            print ('素数有:%d'%(i))  
