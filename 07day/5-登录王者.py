account = 1502050
passwd = 147258
acc = int(input("请输入账号:"))
pwd = int(input("请输入密码:"))
if acc ==account and pwd == passwd:
    print("登录成功")
    s = input("请选择英雄:")
    if s == "ADC":
        print("孙尚香、后裔")
    elif s == "坦克":
        print("廉颇、程咬金")
    elif s == "刺客":
        print("韩信、阿珂")
else:
    print("登录失败")
