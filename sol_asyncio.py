import asyncio
import time

"""
This method uses a traditional asynchronous function 
and achieves concurrency in a while loop with `await asyncio.sleep()`. 

Note: Functions must be added within `main()` and called using `asyncio.run(main())`, 
which may limit flexibility in certain use cases.
"""


async def your_function(timeout):
    start_time = time.time()
    print(f"{timeout} start")
    while True:
        # Achieve concurrency
        await asyncio.sleep(0.1)

        # Check if timeout exceeded
        if timeout and (time.time() - start_time) > timeout:
            print(f"finished {timeout}")
            break


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(your_function(10))
        tg.create_task(your_function(5))
        tg.create_task(your_function(3))


if __name__ == "__main__":
    asyncio.run(main())
