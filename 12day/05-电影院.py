list = []
print("汽车上牌管理系统".center(50,'*'))
while True:
    print("1:添加车主".center(50," "))
    print("2:查找车主".center(50," "))
    print("3:修改车主".center(50," "))
    print("4:删除车主".center(50," "))
    print("5:显示所有用户".center(50," "))
    print("6:退出".center(50," "))
    num = int(input("请选择功能:"))
    if num == 1:
        d = {}
        name = input("请输入车主名字:")
        number =input("请输入车牌号:")
        phone =input("请输入手机号:")
        d["name"] = name 
        d["number"] = number
        d["phone"] = phone
        list.append(d)
        print(list) 
        print("添加成功")
    elif num == 2:
        flag = False
        name = input("请输入你要查的用户:")
        for i in list:
            if name == i["name"]:
                print("用户:%s\n车牌号:%s\n电话%s"%(i["name"],i["number"],i["phone"]))
                flag = True
                break
            if flag == False:
                print("没有此用户")
    elif num == 3:
        name = input("请输入你要修改的用户名:")
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
                    break
            else:
                print("没有此用户")
    elif num == 4:
        name = input("请输入你要删除的用户名:")
        for i in list:
            if name == i["name"]:
                i.clear()
                print("删除成功")
                
    elif num == 5:
        print(list)     
    elif num == 6:
        break       
        
'''         
        for d in list: 
            if d["name"] == a_name:
                print("姓名%s,车牌号%s,手机号%s"%(d['name'],d['number'],d['phone']))
    elif num == 3:
        b_name=input("请输入你要修改的名字:")
        for d in list:
            if d["name"] == b_name:
                d["name"]=input("请输入您修改后的名字:")
                d["number"]=input("请输入你修改后的车牌号:")
                d["phone"]=int(input("请输入你修改后的手机号码:"))
                print(d["name"])
                print("修改成功")
            elif d["name"] !=b_name:
                print("没有这个用户")
    elif num == 4:
        name=input("请输入你要删除的用户:")
        if d['name'] == c_name:
            d.clear()
            print("删除成功:")
    elif num == 5:
        break




'''
'''
                print("1、修改名字")
                print("2、修改车牌号")
                print("3、修改手机号")
                aname = int(input("请选择功能:")) 
                if name == 1:
                    aname=input("请输入新的名字:")
                    d["name"] == name
                elif number == 2:
                    number=input("请输入新的车牌号:")
                    d["number"]== number
                elif aname ==3:
                    phone=input("请输入新的手机号:")
                    d["phone"] == phone
'''
