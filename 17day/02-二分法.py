l = [1,4,7,10,50,57,70,89,100]
min = 0
max = len(l) -1
count = 70
while True:
    print("找了 ")
    center = int((min+max)/2)
    if l[center] > count:
        max = center -1
    elif l[center] < count:
        min = center+1
    elif l[center] == count:
        print("索引是%d"%center)
        break
