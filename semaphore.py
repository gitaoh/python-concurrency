from threading import Semaphore, Thread

import urllib
import urllib.request


MAX_CONCURRENT_DOWNLOADS = 3
semaphore = Semaphore(MAX_CONCURRENT_DOWNLOADS)


def download(url: str):
    with semaphore:
        print(f"Downloading {url}...")
        response = urllib.request.urlopen(url)
        data = response.read()

        print("Finished Downloading...")
        return data


def main():
    urls = [
        "https://www.ietf.org/rfc/rfc791.txt",
        "https://www.ietf.org/rfc/rfc792.txt",
        "https://www.ietf.org/rfc/rfc793.txt",
        "https://www.ietf.org/rfc/rfc794.txt",
        "https://www.ietf.org/rfc/rfc795.txt",
    ]
    threads = []
    for url in urls:
        thread = Thread(target=download, args=(url,))
        threads.append(thread)
        thread.start()

    [t.join() for t in threads]


if __name__ == "__main__":
    main()
