o_sum = 0
j_sum = 0
for i in range(101):
    if i%2==0:
        o_sum+=i
        
for i in range(101):
    if i%2!=0:
        j_sum+=i
        
print("偶数的和是:%d"%o_sum)
print("奇数的和是:%d"%j_sum)
