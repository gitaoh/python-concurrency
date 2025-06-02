from threading import Lock, Thread
from time import sleep

counter = 0

def increase(by, lock: Lock):
    global counter
    
    with lock:
        local_counter = counter
        local_counter+= by

        sleep(0.1)
        counter = local_counter
        print(f"{counter=}")
    


# Creaate a Threading Lock
lock = Lock()

# Create threads
t1 = Thread(target=increase, args=(10,lock))
t2 = Thread(target=increase, args=(20,lock))

# Start the threads
t1.start()
t2.start()

# Wait for the threads to complete
t1.join()
t2.join()


print(f"Final {counter=}")

