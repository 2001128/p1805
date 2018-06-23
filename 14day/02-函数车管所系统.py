list = []
def menu():
        print("1:添加车主".center(50," "))
        print("2:查找车主".center(50," "))
        print("3:修改车主".center(50," "))
        print("4:删除车主".center(50," "))
        print("5:打印车主".center(50," "))
        print("6:退出系统".center(50," "))
#主入口函数
def main():
    print("欢迎使用车管所系统".center(50,"*"))
    while True:
        menu()
        num = int(input("请选择功能"))
        if num == 1:
            add()
        if num == 2:
            find()
        if num == 5:
            print_a()
def add():
    dict = {}
    while True:
        print("1~4位字符")
        name = input("请输入车主名字:")
        if len(name) > 4:
            print("输入不符合规格,请从新输入")
        continue
    while True:
        print("1~7位字符")
        number =input("请输入车牌号:")    
        if len(number) > 7:
            print("输入不符合规格,请从新输入")
        continue
    while True:
        print("11位字符,必须以1开头")
        phone =input("请输入手机号:")
        if len(phone) != 11 or phone.startswith("1") == False:
            print("输入格式有误,请从新输入")
        continue 
        dict["name"] = name
        dict["number"] = number
        dict["phone"] = phone
        list.append(dict)
        print("添加成功")
        break

def print_a():
    print("名字\t\t车牌号\t\t手机号")
    for i in list:
        print(i["name"]+"\t\t"+i["number"]+"\t\t"+i["phone"])
#        print(" %s\t %s\t %s"%(i["name"],i["number"],i["phone"]))
      
main()
'''
def add_card():  
    dict = {}
    num = int(input("请选择功能:"))
    if num == 1:
#    main()
        a = input("添加请按d,退出请按s")
        if a=="d":
            while True:
                name = input("请输入车主的姓名:")
                if len(name) > 4:
                    print("输入不符合规格,请从新输入")
                    break
            number = input("请输入车主的车牌号:")
            
            phone = input("请输入车主的手机号:")
            while True:
                print("11位字符,必须以1开头")
                phone =input("请输入手机号:")
           
                if len(phone) != 11 or phone.startswith("1") == False:
                    print("输入格式有误,请从新输入")
                    break 
            address = input("请输入车主的住址:")
            dict["name"] = name
            dict["number"] = number
            dict["phone"] = phone
            dict["address"] = address
            print("添加成功!")
            list.append(dict)
        elif a=="s":
            print("退出添加系统")
            print(list)
             
main()
'''
