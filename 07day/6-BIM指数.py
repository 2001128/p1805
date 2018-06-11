height = float(input("请输入身高(m):"))
weight = float(input("请输入体重(kg):"))
t = weight/ height**2
if t < 18:
    print("过轻")
elif t >18 and t <25 :
    print("正常")
elif t >=25 and t<28:
    print("过重")
elif t >=28 and t <32:
    print("肥胖")
elif t >=32:
    print("严重肥胖")

