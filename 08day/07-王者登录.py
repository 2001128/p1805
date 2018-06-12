acc = 335775879
pwd = 123456
i = 0
while i<3:
    account = int(input("请输入账号:"))
    passwd = int(input("请输入密码:"))
    if account==acc and passwd==pwd:
        print("登录成功")
        name= int(input("请选择你想玩的英雄类型:0:ADC、1:肉、3:法师"))
        if name ==0:
            print("鲁班大师")
        elif name == 1:
            print("程咬金")
        elif name == 3:
            print("法师")
        break
    else:
        if i!=2:
            print("账号或密码错误 请重新输入")
        else:
            print("账号被冻结")     
        i+=1
       
           # break

