def rs(account,passwd):
    a = ip(account)
    if a:
        print("阿萨德")
def login(account,passwd):
    b = ip(account)
    if b:
        print("阿什利")    
def ip(account):
    if len(account) == 11 and account.startswith("1"):
        return True
    else:
        return False
rs("15811541966","12345678")
login("15811541966","12345678")
