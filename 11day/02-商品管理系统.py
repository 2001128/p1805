print("商品管理系统".center(40,'*'))
list =[]
while True:
    number = int(input("1:添加 2:删除 3:改 4:查 5:退出系统"))
    if number == 1:

        l= []
        
        name =input("请输入商品名称:")
        price =float(input("请输入商品的价格:"))
        l.append(name)
        l.append(price)
        list.append(l)
        print(list)
    elif number == 2:
        
        name = input("请输入你要删除的商品名称:")
        money = float(input("请输入你要删除商品的价格:"))
       # money = float(input("请输入你要删除的价格:"))
        if name in l:
            l.remove(name)
            l.remove(money) 
        else:
            print("查无此人")
    elif number == 3:
        name = input("请输入要修改的商品名称:")
