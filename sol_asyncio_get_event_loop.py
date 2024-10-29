import asyncio
import time

"""
This method uses an asyncio decorator to provide a simple API, 
allowing functions to be called asynchronously while keeping the main thread running. 
Functions executed with this method will operate concurrently.

Note: This method relies on `get_event_loop()`, which is deprecated and 
may be removed in future Python versions. 
Consider updating to a more future-proof approach 
if compatibility with newer versions of Python is required.

Idea from: https://stackoverflow.com/questions/9786102/how-do-i-parallelize-a-simple-python-loop
"""


def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

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
    # Start background tasks
    your_function(10)
    your_function(5)
    your_function(3)

    # Keep the main thread running
    while True:
        time.sleep(1)
