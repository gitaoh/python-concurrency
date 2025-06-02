from concurrent.futures import ThreadPoolExecutor
from time import sleep, perf_counter


def task(id):
    print(f"Starting the task {id}...")
    sleep(1)
    return f"Done with the task {id}"


start = perf_counter()

with ThreadPoolExecutor() as executor:
    results = executor.map(task, [1, 2])
    for result in results:
        print(result)

end = perf_counter()

print(f"Duration: {end - start}s")
