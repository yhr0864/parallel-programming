from mpi4py import MPI
import time
import functools

# Initialize the MPI environment
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Rank of the process
size = comm.Get_size()  # Total number of processes


def run_in_mpi(f):
    """Decorator to handle function execution in parallel with MPI."""

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapped


@run_in_mpi
def your_function(timeout):
    start_time = time.time()
    print(f"[Process {rank}] Task with timeout {timeout} seconds started.")
    while True:
        # Check if timeout exceeded
        if timeout and (time.time() - start_time) > timeout:
            print(f"[Process {rank}] Task with timeout {timeout} finished.")
            break
        time.sleep(0.5)  # Prevents excessive CPU usage


if __name__ == "__main__":
    # Call your_function asynchronously
    your_function(10)
    your_function(5)
    your_function(3)

    # Keep the main thread running
    while True:
        time.sleep(1)
