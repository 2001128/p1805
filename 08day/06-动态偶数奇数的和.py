count = int(input("请输入一个数:"))
o_sum = 0
j_sum = 0
i=0
while i<count:
   # print("当前数字:%d"%i)
    i+=1
    if i%2==0:
        o_sum =o_sum+i
    else:
        j_sum = j_sum+i
print("偶数的和是:%d"%o_sum)
print("奇数的和是:%d"%j_sum)
print("总和为:%d"%(o_sum+j_sum))

