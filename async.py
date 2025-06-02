import asyncio
from time import perf_counter
# from asyncio.exceptions import TimeoutError


async def square(number: int) -> int:
    return number**2


async def main() -> None:
    x = await square(10)
    print(f"{x=}")
    y = await square(5)
    print(f"{y=}")

    print(f"{x+y=}")


class APIError(Exception): ...


async def api(msg: str, r=100, d=4, raise_exception=False):
    print(msg)
    await asyncio.sleep(d)
    if raise_exception:
        raise APIError
    return r


async def show_message():
    for _ in range(3):
        await asyncio.sleep(1)
        print("API call is in progress...")


async def run():
    start = perf_counter()
    # p = await api("GOOGL:", 300)
    # print(p)
    # p = await api("AAPL:", 200)
    # print(p)

    # p = await api("NVDIA:", 400)
    # print(p)

    mt = asyncio.create_task(show_message())

    p1 = asyncio.create_task(api("GOOGL", 300))
    # price = await p1
    # print(price)

    p2 = asyncio.create_task(api("AAPL", 200))
    # price_2 = await p2
    # print(price_2)

    # MAX_TIMEOUT = 3
    # try:
    #     await asyncio.wait_for(asyncio.shield(p2), timeout=MAX_TIMEOUT)
    # except TimeoutError:
    #     print("The task was cancelled due to a timeout")

    p3 = asyncio.create_task(api("TSLA", 700))
    # if not p3.done():
    #     print("Cancelling the task...")
    #     p3.cancel()

    # price_3 = await p3
    # print(price_3)

    # time_elapsed = 0
    # while not p3.done():
    #     time_elapsed += 1
    #     await asyncio.sleep(1)
    #     print("Task not completed, checking again in a second")
    #     if time_elapsed == 3:
    #         print("Cancelling the task...")
    #         p3.cancel()
    #         break

    try:
        await mt
    except asyncio.CancelledError:
        print("Show Message has been cancelled")

    pending = (p1, p2, p3, mt)
    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        result = done.pop().result()
        print(result)

    end = perf_counter()
    print(f"Duration: {end - start}s")


if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(run())
