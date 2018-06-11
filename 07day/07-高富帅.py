sex = input("请输入你的性别:")	
if sex == "男":
	h = input("请输入身高:")
	m =int(input("请输入财富:"))
	y = input("请输入颜值:")
	if h > "180" and m > 1000 and y >"90":
		print("高富帅")
    else:
        print("屌丝")
elif sex == "女":
	c = input("请皮肤颜色:")
	m = int(input("请输入财富:"))
	y = input("请输入你的颜值:")
	if c == "白色" and m > 800 and y > "90":
		print("白富美")
	else:
		print("哈哈")
