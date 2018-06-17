list= ["laowang","laogao","laozhao","laowang"]
name = input("请输入你要查询的名字:")
    
count = 0
for i in list:
    if name == i:
        print("找到了索引是%d"%count)
    count+=1




for position, i in enumerate(list):
    if name == i:
         print(position,i)  
