import os

os.environ["RAY_DEDUP_LOGS"] = "0"


import ray
import time
import functools


# Initialize Ray
ray.init(ignore_reinit_error=True)


def background(f):
    """Decorator to run a function as a Ray remote task."""
    f_remote = ray.remote(f)  # Convert function to a Ray remote function

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        # Call the remote function asynchronously
        return f_remote.remote(*args, **kwargs)

    return wrapped


@background
def your_function(timeout):
    start_time = time.time()
    print(f"Task with timeout {timeout} started.")
    while True:
        if timeout and (time.time() - start_time) > timeout:
            print(f"Task with timeout {timeout} finished.")
            break


if __name__ == "__main__":
    # Call your_function asynchronously
    your_function(10)
    your_function(5)
    your_function(3)

    # Keep the main thread running
    while True:
        time.sleep(1)
