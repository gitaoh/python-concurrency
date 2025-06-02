from asyncio import create_task, run, sleep, Future


async def plan(plan: Future) -> None:
    print("Planning my future....")
    await sleep(1)
    plan.set_result("Bright")


def create() -> Future:
    f = Future()
    create_task(plan(f))
    return f


async def main():
    t = create()
    result = await t
    print(result)


if __name__ == "__main__":
    run(main())
