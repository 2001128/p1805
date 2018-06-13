import random
a_money = 0
for i in range(1,30):
    for j in range(1,3):
        km = random.randint(1,33)
        if km <= 6:
            price = 3
        elif km >6 and km <=12:
            price = 4 
        elif km > 12 and km <=22:
            price = 5 
        elif km >22 and km <=32:
            price = 6
        elif km > 32:
            if (km-32)%20 == 0:
                price = 6+(km-32)/20
            else:
                price = 6+int((km-32)/20)+1   
        if a_money > 100 and a_money <=150:
            a_money = a_money*0.8
        elif a_money >150 and a_money<=400:
            a_money = a_money*0.5
        elif a_money >400:
            a_money = price*1
        a_money = a_money+ price
print("总额%.02f"%a_money)

     
        
        
