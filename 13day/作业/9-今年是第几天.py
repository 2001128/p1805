'''
def com_days(year,month,day):#形参
    big_month = [1,3,5,7,8,10,12]#大月
    small_month = [4,6,9,11]#小月
    days = 0#默认一共0天
    for i in range(1,month):
        if i in big_month:
            days+=31
        elif i in small_month:
            days+=30
        if i == 2:#特殊二月,判断闰年平年
            if (year%4 ==0 and year%100 != 0) or year%400 == 0:
                days +=29
            else:
                days +=28
    days+=day
    print("一共%d天"%days)
date = "20180622"
year = int(date [:4])
month = int(date [4:6])
day = int(date[6:8])
com_days(year,month,day)
'''
def com(year,month,day):
    da_month = [1,3,5,7,8,10,12]
    xiao_month = [4,6,9,11]
    days = 0
    for i in range(1,month):
        if i in da_month:
            days+=31
        if i in xiao_month:
            days+=30
        if i == 2:
            if (year%4 == 0 and year%100 !=0) or year%400 == 0:
                days+=29
            else:
                days+=28
    days+=day
    print("一共有%d天"%days)
    
date = "20181008"
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])
com(year,month,day)

