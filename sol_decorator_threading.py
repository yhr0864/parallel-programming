import threading
import functools
import time


def decorator_parallel(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


@decorator_parallel
def your_function(time_for_sleep):
    print(f"func with {time_for_sleep} started")
    time.sleep(time_for_sleep)
    print(f"func with {time_for_sleep} finished")


if __name__ == "__main__":

    your_function(10)
    your_function(5)
    your_function(3)

    # Keep the main thread running
    while True:
        time.sleep(1)
