'''
c = ["小王","小李","小张"]
for i in c:
    print(i)
#add data 添加数据
#remove data 删除数据
#change data 修改数据
#find data 查数据
c.append("齐天大圣")#把列表和字符串当做一个值 插入到列表当中
print(c)
c.insert(0,"唐僧")#增加插入
print(c)
c.extend("天蓬元帅")#分别插入列表中
print(c)
'''
void = []
for i in range(101):
    if i%2!=0:
     #   print(i)
        void.append(i)
print(void)

void.pop()#删除最后一个
void.pop(0)#删除指定索引的值
del void[0]#系统提供的删除方法
void.remove(7)#删除指定的值
#void.insert(0,"唐僧")
print("删除后",void)
       


