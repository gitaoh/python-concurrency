from threading import Thread
from time import sleep


def show_timer(): 
    count = 0
    while True:
        count += 1
        sleep(1)
        print(f"Has been waiting for {count} seconds....")


t = Thread(target=show_timer, daemon=True)
t.start()

ans = input("Exit Y/N: \n")
