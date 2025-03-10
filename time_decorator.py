import time
import tracemalloc
import functools

def complexity_profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        time_taken = end_time - start_time

        print(f"🔹 Function: {func.__name__}")
        #print(f"🧮 Parameters: {func.__dict__}")
        print(f"Arguments are: {args}")
        print(f"⏳ Time Taken: {time_taken:.6f} sec")
        print(f"💾 Peak Memory Used: {peak / 1024:.4f} KB")

        # Approximate complexity based on execution time
        if time_taken < 1e-6:
            print("🟢 Likely O(1) or O(log N) complexity")
        elif time_taken < 1e-3:
            print("🟡 Likely O(N) complexity")
        elif time_taken < 1:
            print("🟠 Likely O(N log N) or O(N²)")
        else:
            print("🔴 Likely O(2^N) or worse complexity")

        print(result)

    return wrapper

'''
from time_decorator import complexity_profiler

@complexity_profiler
'''