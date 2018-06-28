l = []
def sy():
    while True:
        print('车管所管理系统'.center(50,'*'))
        print('1.添加车主'.center(50," "))
        print('2.查找车主'.center(50," "))
        print('3.修改车主'.center(50," "))
        print('4.删除车主'.center(50," "))
        print('5.显示车主'.center(50," "))
        print('6.退出系统'.center(50," "))
        n = int(input('请选择功能'))
        if n == 1:
            append()
        elif n == 2:
            find()
        elif n == 3:
            revise()
        elif n == 4:
            remove()
        elif n == 5:
            print_a()
        else:
            break
        
def append():#添加车主
    d = {}
    while True:
        print("2~4位字符")
        name = input('请输入车主姓名:')
        if len(name) >=2 and len(name) <=4: #and len(name) >2 == False:
            break
        else:
            print('格式不对,请重新输入')
            continue
    while True:
        print("7位字符")
        number = input('请输入车主的车牌号:')
        if len(number) == 7:
            break
        else:
            print('格式不对,请重新输入')
            continue
    while True:
        print("11位字符,必须以1开头")
        phone = input('请输入要添加的手机号')
        if len(phone) == 11 and phone.startswith('1') == True:
            break
        else:
            print('格式有误')
            continue
    while True:
        print("2~7位字符,只输入省份")
        adress = input("请输入你的家庭住址:")
        if len(adress) >2 and len(adress)<=7:
            break
        else:
            print("格式不对")
            continue
    while True:
        d['name']=name
        d['number']=number
        d['phone']=phone
        d['adress']=adress
        l.append(d)
        print('添加成功')
        break
def find():#查找车主
    
    flag = False
    a_name = input('请输入要查找的车主姓名:')
    b_name = input("请输入你要找的车主手机号:")
    for d in l:
        if a_name == d['name'] and b_name == d["phone"]:
            print('姓名%s,车牌号%s,手机号%s,家庭地址%s'%(d['name'],d['number'],d['phone'],d["adress"]))
            flag = True
            break
    if flag == False:
        print('查无此人')
def revise():#修改车主
    b_name = input("请输入你要修改的用户名:")
    c_phone = input("请输入你要修改用户名的手机号:")
    flag = False
    for i in l:
        if b_name == i["name"] and c_phone == i["phone"]:
            print("1、修改名字")
            print("2、修改车牌号")
            print("3、修改手机号")
            print("4、修改家庭住址")
            name = int(input("请选择功能:"))
            if name == 1:
                while True:
                    print("2~4位字符")
                    i["name"] = input("请输入新用户:")
                    if len(i["name"]) >=2 and len(i["name"]) <5: #and len(name) >2 == False:
                        print("修改成功")
                        break
                    else:
                        print('格式不对,请重新输入') 
                       # continue
            elif name == 2:
                while True:
                    print("7位字符")
                    i["number"] = input("请输入新的车牌号:")
                    if len(i["number"]) == 7:
                        print("修改成功")
                        break
                    else:
                        print('格式不对,请重新输入')
                            #continue
            elif name == 3:
                while True:
                    print("11位字符,必须以1开头")
                    i["phone"] = input("请输入新的手机号:")
                    if len(i["phone"]) == 11 and i["phone"].startswith('1') == True:
                        print("修改成功")
                        break
                    else:
                        print('格式有误')
                           # continue
            elif name == 4:
                while True:
                    print("2~7位字符,只输入省份")
                    i["adress"] = input("请输入你的新地址:")
                    if len(i["adress"]) >2 and len(i["adress"])<=7:
                        break
                    else:
                        print("格式不对")
                            #continue
                    print(i["name"])
            flag = True
            break
    if flag == False:
        print("没有此用户")
def remove():#删除车主
    name = input('请输入要删除的车主名字:')
    phone = input("请输入你要删除的车主电话:")
    flag = False
    for position,i in enumerate(l):
        if name == i['name'] and phone == i["phone"] :
        
            print('1:确认删除')
            print('2:取消删除')
            n = int(input('请选择'))
            if n == 1:
                l.pop(position)
                print("删除成功")
            break
    if flag == False:
        print('查无此人')
def print_a():#显示车主
    print('名字\t 车牌号\t\t电话\t\t家庭住址\t')
    for i in l:
        print(i['name']+"\t"+i["number"]+"\t"+i["phone"]+"\t"+i["adress"])
sy()

