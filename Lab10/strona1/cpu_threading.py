import concurrent.futures
import time
from strona1.cpu_concurrent import cpu_bound


def find_sums_threading(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)

numbers = [5_000_000 + x for x in range(20)]

start_time = time.time()
find_sums_threading(numbers)
duration_cpu_bound_threads = time.time() - start_time
print(f"Duration {duration_cpu_bound_threads} seconds")