from threading import Thread
from time import sleep, perf_counter


def task(id):
    print(f"Starting task({id})....")
    sleep(1)
    print("Done")


start = perf_counter()

# Create and start 10 threads
threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

# wait for the threads to complete
for t in threads:
    t.join()

# Create two new Threads
# thread_1 = Thread(target=task, args=(1,))
# thread_2 = Thread(target=task, args=(2,))

# Start the threads
# thread_1.start()
# thread_2.start()

# Wait for the threads to complete
# thread_1.join()
# thread_2.join()

# task()
# task()
end = perf_counter()

print(f"Duration: {end - start}s")
