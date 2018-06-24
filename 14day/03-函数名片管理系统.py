list = []#存放名字
def zhuce():
    while True:
        print('名片管理系统'.center(50,'*'))
        print('1.添加名片'.center(50," "))
        print('2.查找名片'.center(50," "))
        print('3.修改名片'.center(50," "))
        print('4.删除名片'.center(50," "))
        print('5.显示全部名片'.center(50," "))
        print('6.退出'.center(50," "))
        n = int(input('请选择功能'))
        if n == 1:
            yi()
        elif n == 2:
            er()
        elif n == 3:
            san()
        elif n == 4:
            si()
        elif n== 5:
            wu()
        else:
            break
        
def yi():
    d = {}
    while True:
        name = input('请输入要添加的名字')
        if len(name) <= 4:
            break
        else:
            print('格式不对')
            continue
    while True:
        job = input('请输入要添加的职位')
        if len(name) <= 6:
            break
        else:
            print('格式不对')
            continue
    while True:
        phone = input('请输入要添加的手机号')
        if len(phone) != 11 or phone.startswith('1') == False:
            print('格式有误')
            continue
        d['name']=name
        d['job']=job
        d['phone']=phone
        list.append(d)
        print('添加成功')
        break
def er():
    flag = False
    f_name = input('请输入要查找的姓名')
    for d in list:
        if d['name'] == f_name:
            print('姓名%s,工作%s,手机%s'%(d['name'],d['job'],d['phone']))
            flag = True
            break
        if flag == False:
            print('查无此人')
def san():
    x_name = input('请输入要修改的名片')
    for d in list:
        if x_name == d['name']:
            d['name']=input('请输入您修改后的名字')
            d['job']=input('请输入您修改后的工作')
            d['phone']=input('请输入您修改后的手机号')
        flag = True
        break
    if flag == False:
        print('查无此人')
def si():
    s_name = input('请输入要删除的名字')
    flag = False
    for position,i in enumerate(list):
        if name == i['name']:
            print('1:确认删除')
            print('2:取消删除')
            n = int(input('请选择'))
            if n == 1:
                list.pop(position)
            break
        if flag == False:
            print('查无此人')
def wu():
    print('名字\t职位\t电话\t')
    for i in list:
        print(i['name']+"\t "+i['job']+"\t "+i['phone'])
zhuce()

  
