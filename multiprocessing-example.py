from multiprocessing import Process
from time import perf_counter


def task():
    res = 0
    for _ in range(10**8):
        res += 1
    return res


if __name__ == "__main__":
    start = perf_counter()
    ps = [Process(target=task) for i in range(2)]
    [p.start() for p in ps]
    [p.join() for p in ps]

    # task()
    # task()
    end = perf_counter()

    print(f"Duration: {end - start}s")
