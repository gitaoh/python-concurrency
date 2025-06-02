from threading import Lock, Thread
from time import perf_counter, sleep


class Counter:
    def __init__(self) -> None:
        self.value = 0
        self.lock = Lock()

    def increase(self, by):
        with self.lock:
            current = self.value
            current += by
            sleep(0.1)
            self.value = current
            print(f"Counter: {self.value}")


def main():
    counter = Counter()

    # create threads
    t1 = Thread(target=counter.increase, args=(10,))
    t2 = Thread(target=counter.increase, args=(20,))

    # Start the threads
    t1.start()
    t2.start()

    # Wait for the threads to complete
    t1.join()
    t2.join()
    print(f"Final: {counter.value}")


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Duration: {end - start}s")
