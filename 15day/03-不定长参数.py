def d_sum (a,b,*args,**kwargs):
#    print(a)
#   print(b)
    s = 0
    for i in args:
        s += i
    c = s+a+b
    v = 0   
 #   print(args)
    for i in kwargs.values():
        v += i
        print(v+c) 

  #  print(kwargs)

t = {1,2,3,4,5,6,}
d = {"age":12,"weight":24}
d_sum(1,2,*t,**d)   
