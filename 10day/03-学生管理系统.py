list = []
while True:
    P = int(input("请选择功能:1:添加 2：删除 3:修改 4:查找"))
    if P ==1:
        u = input("请输入你要添加的名字:")
        list.append(u)
        print(list)
    elif P ==2:
        name = (input("请输入你要删除名字:"))
        if name in list:
            list.remove(name)
        else:
            print("没有这个人")
        print(list)
    elif P ==3:
        name = input("请输入你要修改的名字:")
        if name in list:
            position = list.index(name)
            name = input("请输入新的名字:")
            list[position] = name
        else:
            print("查无此人")
'''
        user=input("请输入你要查找的名字:")
        if user in list:
            b=list.index(user)
            list[int(input("请输入下标:"))]
            n=input("请输入你的新名字:")
            list[b]=n
            print(list)
        else:
            print("没有这个人")
'''
    elif P ==4:
        name =input("请输入你要查找的名字:"))
        if name in list:
            position = list.index(name)
            print("你要查找的人的索引是%d"%position)
        else:   
            print("查无此人")
    print(list)   
        break    
        
        
  
  
    
