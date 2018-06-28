list = [15,49,7,40,100,60,2,1,3]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list [j]:
            list[i],list[j] = list[j],list[i]
    print(list)

