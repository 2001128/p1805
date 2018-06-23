list= []
print("汽车上牌管理系统".center(50,'*'))
while True:
    print("1:添加车主".center(50," "))
    print("2:查找车主".center(50," "))
    print("3:修改车主".center(50," "))
    print("4:删除车主".center(50," "))
    print("5:打印车主".center(50," "))
    print("6:退出".center(50," "))
    num = int(input("请选择功能:"))
    if num == 1:
        d = {}
        while True:
            print("1~4位字符")
            name = input("请输入车主名字:")
            #print("1~4位字符")
            if len(name) > 4:
                print("输入不符合规格,请从新输入")
                break
        while True:
            print("1~7位字符")
            number =input("请输入车牌号:")
           # print("1~7位字符")
            if len(number) > 7:
                print("输入不符合规格,请从新输入")
                break
        while True:
            print("11位字符,必须以1开头")
            phone =input("请输入手机号:")
           # print("11位字符,必须以1开头")
            if len(phone) != 11 or phone.startswith("1") == False:
                print("输入格式有误,请从新输入")
                break 
            d["name"] = name
            d["number"] = number
            d["phone"] = phone
           
            list.append(d)
            print(list) 
            print("添加成功")
             
    elif num == 2:
        name = input("请输入你要查的用户:")
        flag = False
        for i in list:
            if name == i["name"]:
                print("用户:%s\n车牌号:%s\n电话%s"%(i["name"],i["number"],i["phone"]))
                flag = True
                break
        if flag == False:
            print("没有此用户")
    elif num == 3:
        name = input("请输入你要修改的用户名:")
        flag = False
        for i in list:
            if name == i["name"]:
                print("1、修改名字")
                print("2、修改车牌号")
                print("3、修改手机号")
                name = int(input("请选择功能:"))
                if name == 1:
                    i["name"] = input("请输入新用户:") 
                elif name == 2:
                    i["number"] = input("请输入新的车牌号:")
                elif name == 3:
                    i["phone"] = input("请输入新的手机号")
                    print(i["name"])
                flag = True
                break
        if flag == False:
            print("没有此用户")
    elif num == 4:
        name = input("请输入你要删除的用户名:")
        flag = False
        for position,i in enumerate(list):
            if name == i["name"]:
                flag = True
                print("1:确认删除")
                print("2:取消删除")
                num_1 = int(input("请选择序号:"))
                if num_1 == 1:
                    list.pop(position)
                break
                print("删除成功")
        if flag == False:
            print("没有此用户")
    elif num == 5:
        print("名字\t职位\t电话")
        for i in list:
            print(i["name"]+"\t"+i["number"]+"\t"+i["phone"])
                 
    elif num == 6:
        break

       
        
