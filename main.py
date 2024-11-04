from sol_async_without_run import *

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

print("started main")
start_time = time.time()
while True:
    # Check if timeout exceeded
    if (time.time() - start_time) > 3:
        print("finished main")
        break

# Start background tasks
your_function(10)
your_function(5)
your_function(3)

# Keep the main thread running
while True:
    time.sleep(1)
