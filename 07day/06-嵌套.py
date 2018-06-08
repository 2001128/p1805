print("请选择你要玩的游戏:")
game = input ("1:王者荣耀 2:植物大战僵尸")

pwd = "123456"
account = "123456"
if game == "1":
	acc = input("请输入账号:")
	p = input("请输入密码:")
	if acc == account and p == pwd:
		print("登陆成功，欢迎来到王者荣耀")
	else:
		print("登录失败")
elif game == "2":
	print("一大波僵尸正在来袭")
else:
	print("错误的操作")
	
	
	
