'''
i = 1
while i <24:
    print("玩游戏%d小时"%i)
    if i == 8:
        print("你爸来了")
        break
    i+=1
'''
j = 0
while j<23:
    j+=1
    if j == 8:
        print("你爸来了")
        continue
    print("玩游戏%d"%j)
