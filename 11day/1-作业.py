import random
a = ['新年快乐', '岁岁平安','大吉大利']
b = ['端午快了', '端午安康','前程似锦']
c = ['圣诞快乐', '灵动的雪花','漫天飞舞']
festival= input("请输入节日:")
if festival=="新年":
    print("一月一日")
    d=random.sample(a,random.randint(2,2))
    print(d)
elif festival== "端午":
    print("五月初五")
    e=random.sample(b,random.randint(2,2))
    print(e)
elif festival == "圣诞":
    print("十二月二十五")
    f=random.sample(c,random.randint(2,2))
    print(f)

    
