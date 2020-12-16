import asyncio
import nest_asyncio
import time

async def find_sum_asyncio(numbers):
    tasks=[]
    for number in numbers:
        task = asyncio.ensure_future(cpu_bound_asyncio(number))
        tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)


async def cpu_bound_asyncio(number):
    return sum(i * i for i in range(number))

sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
numbers = [5_000_000 + x for x in range(20)]
start_time = time.time()
nest_asyncio.apply()
asyncio.run(find_sum_asyncio(numbers))
duration_cpu_bound_asyncio = time.time() - start_time
print(f"Downloaded {len(sites)} sites in {duration_cpu_bound_asyncio} seconds")