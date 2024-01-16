
import time

def global_timer():
    while True:
        global_time = time.time()
        print(global_time)
        time.sleep(1)



if __name__ == "__main__":
    global_timer()