from time import perf_counter
from lxml import html
import requests
from datetime import datetime


def get_month(month):
    return {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }[month]


def main() -> None:
    URL = {
        "DAILY": "https://finance.yahoo.com/quote/META/history/?frequency=1d&period1=1337347800&period2=1748801863",
        "WK": "https://finance.yahoo.com/quote/META/history/?frequency=1wk&period1=1337347800&period2=1748801863&filter=history",
        "MON": "https://finance.yahoo.com/quote/META/history/?frequency=1mo&period1=1337347800&period2=1748801863&filter=history"
    }
    res = requests.get(
        URL["MON"],
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        },
    )
    csv_data = []
    if res.status_code == 200:
        data = html.fromstring(res.text)
        xpath = '//*[@id="nimbus-app"]/section/section/section/article/div[1]/div[3]/table/tbody'
        body = data.xpath(xpath)[0]
        rows = body.findall("./tr")
        for row in rows:
            td = row.findall("./td")
            if len(td) <= 2:
                continue
            r_data = []
            for i, r in enumerate(td):
                if i == 0:
                    date = str(r.text)
                    md, s, y = date.partition(",")
                    m, d = md.split(" ")
                    m = get_month(str(m).lower())
                    obj = datetime(year=int(y), month=m, day=int(d))
                    formatted_date = obj.strftime("%m/%d/%Y")
                    r_data.append(formatted_date)
                elif i == 6:
                    num = str(r.text)
                    num = num.replace(',', "")
                    r_data.append(num)
                else:
                    r_data.append(r.text)
            csv_data.append(r_data)

    with open("data-mon.csv", "w+") as f:
        cols = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
        f.write(f"{','.join(cols)},\n")

        for data in csv_data:
            f.write(f"{','.join(data)},\n")


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Duration: {end - start}s")
