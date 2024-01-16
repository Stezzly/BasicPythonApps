
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

def stopwatch():
    start_time = time.time()
    input("Stopwatch started. Press Enter to stop.")
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


#global_timer()
#countdown_timer()
stopwatch()