from threading import Event, Thread
from time import sleep


def task(event: Event):
    for i in range(6):
        print(f"Running #{i + 1}")
        sleep(1)
        if event.is_set():
            print("The thread was stopped permaturely")
            break
    else:
        print("The thread was stopped maturely")


def main() -> None:
    event = Event()

    thread = Thread(target=task, args=(event,))
    thread.start()
    sleep(3)
    event.set()


# Stopping a thread that uses a child class of the Thread class
class Worker(Thread):
    def __init__(self, event: Event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event


    def run(self) -> None:
        for i in range(6):
            print(f"Running #{i+1}")
            sleep(1)
            if self.event.is_set():
                print("The thread was stopped prematurely")
                break
        else:
            print("Thread was stopped maturely")

def run() -> None:
    e = Event()    
    t = Worker(e)
    t.start()
    sleep(3)
    e.set()

if __name__ == "__main__":
    # main()
    run()
