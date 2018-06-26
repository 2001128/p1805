'''
list = []
def su(x,y):
    for i in range(x,y+1):
        flag = 0
        for j in range(2,i):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            list.append(i)
           # return list
    print(list)
su(2,200)
'''
def su():
    l = []
    for i in range(2,201):
        flag = 0
        for j in range(2,i):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            l.append(i)
    return l
res = su()
print(res)
        
