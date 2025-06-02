from threading import Event, Thread
from time import perf_counter, sleep
from urllib import request


def task(event: Event, id: int) -> None:
    print(f"Thread {id} started. Waiting for the signal...\n")
    event.wait()
    print(f"Received Signal. The thread {id} was completed\n")


def main() -> None:
    event = Event()

    # Threads
    t1 = Thread(target=task, args=(event, 1))
    t2 = Thread(target=task, args=(event, 2))

    # Start Threads
    t1.start()
    t2.start()

    print("Blocking the main thread for 3 Seconds...")
    sleep(3)
    event.set()


def download(url: str, event: Event) -> None:
    print(f"Downloading file from {url}")
    _, _ = request.urlretrieve(url, "rfc793.txt")
    # Download Complete
    event.set()


def process(event: Event):
    print("Waiting for the file to be downloaded...")
    event.wait()

    print("File downloaded completed. Starting file processing...")

    count = 0
    with open("rfc793.txt", "r") as file:
        for line in file:
            words = line.split()
            count += len(words)

    print(f"Number of words in the file: {count}")


def run():
    event = Event()
    dl = Thread(target=download, args=("https://www.ietf.org/rfc/rfc793.txt", event))
    dl.start()

    # Create and start the file processing thread
    proc = Thread(target=process, args=(event,))
    proc.start()

    # Wait for the both threads to complete
    dl.join()
    proc.join()

    print("Main thread finished")


if __name__ == "__main__":
    start = perf_counter()
    # main()
    run()
    end = perf_counter()
    print(f"Duration: {end - start}s")
