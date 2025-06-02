from queue import Empty, Queue
from threading import Thread
from time import sleep


def producer(queue: Queue):
    for i in range(1, 6):
        print(f"Inserting item {i} into the queue")
        sleep(1)
        queue.put(i)


def consumer(queue: Queue):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f"\nProcessing item {item}")
            sleep(2)
            queue.task_done()


def main():
    queue = Queue()

    pt = Thread(target=producer, args=(queue,))
    pt.start()

    ct = Thread(target=consumer, args=(queue,), daemon=True)
    ct.start()

    pt.join()
    queue.join()


if __name__ == "__main__":
    main()
