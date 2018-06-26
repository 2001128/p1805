
def a_num(num):
    if num == 1:
        return 1
    else:
        return num*a_num(num-1)
result = a_num(10)
print(result)
'''
def cul_num(num):
    num*cul_num(num-1)
    
def cul_num(num):
    num*cul_num(num-1)
def cul_num(num):
    num*cul_num(num-1)
    
def cul_num(num):
    num*cul_num(num-1)
result = cul_num(10)
print(result)
'''


