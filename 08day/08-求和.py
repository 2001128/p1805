'''i = 0
j_sum = 0
while i <100:
    if i % 2!=0:
        j_sum += i
        i += 2  
        print(j_sum)

a=0
o_sum=0
while a<=100:
    if a%2==0:
        o_sum +=a
        a +=2
        c = o_sum   
        d = j_sum-o_sum
        print("1-2+3-4+5-6+7-8...+99的和%s:"%d) 
  '''
i = 1
a_sum = 0
while i<100:
    if i % 2 ==0:
        a_sum=a_sum - i
    else:
        a_sum=a_sum + i
    i+=1
print(a_sum)


    
