import time
def play_game1():
    i = 1
    if i%2 !=0:
        print("我喜欢写代码")
        i+=2
def play_game():
    i=0
    while  True:
        print("我喜欢玩游戏")
        i+=2
        play_game1()
        time.sleep(0.5)           
play_game()
    
    
