l=[]
a_sum = 0
for i in range(100,201):
    flag = 1
    for j in range(2,i):
        if i%j == 0:
            flag = 0
            break
    if flag == 1:
        a_sum+=i
       # print("总和%d"%a_sum) 
        l.append(i)
print(l)
#l.append(a_sum)
#print("总和:"a_sum)
l.insert(0,"100~200之间素数的和为:%s"%a_sum)
print(l)
l.pop(0)
print(l)

l.sort(reverse = False) 
print("降序",l)
l.reverse()
print("倒序",l) 
