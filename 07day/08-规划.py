xq = input("请输入星期几:")
if xq == "1" or xq == "2"or xq == "3"or xq =="4"or xq=="5":
	day = input("请输入上午还是下午:")
	if day == "上午":
		s = int(input("请输入时间:"))
		if  s >=8 and s<10:
			print("正在上课")
		elif s >= 10 and s<12:
			print("正在玩游戏")
	if day == "下午":
		s = int(input("请输入时间:"))
		if s >14 and s<17:
			print("正在上课")
		else:
			print("不知道在干什么")
if xq=="6":
	print("全天上课")
elif xq=="7":
	print("逛街")
