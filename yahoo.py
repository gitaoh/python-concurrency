from threading import Thread
from time import perf_counter
import requests
from lxml import html


class Stock(Thread):
    def __init__(self, symbol: str) -> None:
        super().__init__()
        self.symbol = symbol
        self.url = f"https://finance.yahoo.com/quote/{symbol}"
        self.price = None

    def run(self) -> None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            # Parse the HTML
            tree = html.fromstring(response.text)

            # Get the price in text
            xpath = '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span/text()'
            price_text = tree.xpath(xpath)

            if price_text:
                try:
                    self.price = float(price_text[0].replace(",", ""))
                except ValueError:
                    self.price = None

    def __str__(self) -> str:
        return f"{self.symbol}\t{self.price}"


def main() -> None:
    symbols = ["MSFT", "GOOGL", "AAPL", "META"]
    threads = [Stock(s) for s in symbols]
    [t.start() for t in threads]
    [t.join() for t in threads]
    [print(t) for t in threads]


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Duration: {end - start}s")
