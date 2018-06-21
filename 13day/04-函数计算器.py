#sum = 0
def print_value(x,y,f):#形参
   # x = int(input("请输入第一个值:"))
   # y = int(input("请输入第二个值:"))
   # f = input("请输入运算符:")
    if f == "+":
        print("和是:%d"%(x+y))
    elif f == "-":
        print("差是:%d"%(x-y))
    elif f == "*":
        print("积是:%d"%(x*y))
    elif f == "/":
        if y != 0:
            print("商是%f"%(x/y))
        else:
            print("输入不合法")
        
x = int(input("请输入第一个值:"))
y = int(input("请输入第二个值:"))
f = input("请输入运算符+-*/:")
print_value(x,y,f)#实参
