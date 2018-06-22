list = []

def add_card():
    if num == 1:
        dict = {}
        name = input("请输入车主的姓名:")
        number = input("请输入车主的车牌号:")
        phone = input("请输入车主的手机号:")
        address = input("请输入车主的住址:")
        dict["name"] = name
        dict["number"] = number
        dict["phone"] = phone
        dict["address"] = address
        list.append(dict)
        print(list)
def main():
    print("欢迎使用车管所系统".center(50,"*"))
    print("1:添加车主".center(50," "))
    print("2:查找车主".center(50," "))
    print("3:修改车主".center(50," "))
    print("4:删除车主".center(50," "))
    print("5:打印车主".center(50," "))
    print("6:退出".center(50," "))
    num = int(input("请选择功能:"))
add_card()  
