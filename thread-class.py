from threading import Thread

from time import perf_counter
import urllib
import urllib.error
import urllib.request


class HTTPRequest(Thread):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    def run(self) -> None:
        print(f"Checking: {self.url}")

        try:
            response = urllib.request.urlopen(self.url)
            print(response.code)
        except urllib.error.HTTPError as e:
            print(e.code)
        except urllib.error.URLError as e:
            print(e.reason)


def main() -> None:
    urls = ["https://httpstat.us/200", "https://httpstat.us/400"]
    threads = [HTTPRequest(url) for url in urls]
    [t.start() for t in threads]
    [t.join() for t in threads]

if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Duration: {end-start}s")
