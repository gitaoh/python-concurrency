from asyncio import gather, run, sleep


class APIError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


async def api_failed():
    await sleep(3)
    raise APIError("API failed")


async def api(message: str, result, delay=3):
    print(message)
    await sleep(delay)
    return result


async def main():
    a, b, c = await gather(
        api("API-1", 100), api("API-2", 200), api_failed(), return_exceptions=True
    )
    print(a, b, c)


run(main())
