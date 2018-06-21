list = []
def register(acc,pwd):
    user = {}
    if len(acc) == 11 and acc.startswith("1") and len(pwd) > 6:
        print("注册成功") 
        user["acc"] = acc
        user["pwd"] = pwd
        list.append(user)
            
    else:
        print("注册失败")
         
acc = input("注册账号:")
pwd = input("注册密码:")
register(acc,pwd)

def login(acc,pwd):
    for i in list:
        if acc == i["acc"] and pwd == i["pwd"]:
            print("登录成功")
        else:
            print("登录失败")

if list:
    acc = input("请输入账号:")
    pwd = input("请输入密码:")
    login(acc,pwd)
    
    
