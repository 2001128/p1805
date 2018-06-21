 = {'name':'董帅','birthday':'2001.1.28','sex':'男','address':'山东菏泽','habby':'跑步'}   
#第一种方法:
for k,v in d.items():
    print(k,v)


#第二种方法:
for i in d.items():
    for j in i:
        print(j) 
