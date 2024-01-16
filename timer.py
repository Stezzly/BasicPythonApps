
import time

def global_timer():
    while True:
        global_time = time.time()
        print(global_time)
        time.sleep(1)

def countdown_timer(seconds):
    while True:
        print(seconds)
        time.sleep(1)
        seconds -=1

if __name__ == "__main__":
    #global_timer()
    countdown_timer(60)