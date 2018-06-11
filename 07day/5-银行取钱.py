account = 1502050
passwd = 147258
money = 100000
acc = int(input("请输入账号:"))
pwd = int(input("请输入密码:"))
if acc == account and pwd == passwd:
    print("登录成功")
    mo = int(input("请输入取款金额:"))
    if mo > money:
        print("没钱取鸡毛")
    else:
        print("取了%d元，还剩%s元"%(mo,money-mo))
#elif acc != account and pwd != passwd:
else:
    print("非法账户")

