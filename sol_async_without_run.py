import asyncio
import time
import functools

"""
This method utilizes an asyncio decorator to provide a straightforward API, 
enabling functions to be called asynchronously while the main thread continues running. 
Functions invoked through this method will execute concurrently.

Note: This implementation no longer uses the deprecated `get_event_loop()`, 
making it a more future-proof choice for most cases.
"""


def background(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_in_executor(None, f, *args, **kwargs)

    return wrapped


@background
def your_function(timeout):
    start_time = time.time()
    print(f"{timeout} start")
    while True:
        # Check if timeout exceeded
        if timeout and (time.time() - start_time) > timeout:
            print(f"finished {timeout}")
            break


if __name__ == "__main__":
    # Create and set the event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Start background tasks
    your_function(10)
    your_function(5)
    your_function(3)

    # Keep the main thread running
    while True:
        time.sleep(1)
