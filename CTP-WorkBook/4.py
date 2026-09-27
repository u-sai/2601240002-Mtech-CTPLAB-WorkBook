import time
import tracemalloc


def list_processing(n: int) -> int:
    data = [i * i for i in range(n)]
    return sum(data)


def generator_processing(n: int) -> int:
    data = (i * i for i in range(n))
    return sum(data)


n = 1_000_000


tracemalloc.start()

start = time.perf_counter()
list_result = list_processing(n)
list_time = time.perf_counter() - start

_, list_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()


tracemalloc.start()

start = time.perf_counter()
generator_result = generator_processing(n)
generator_time = time.perf_counter() - start

_, generator_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()


print("List Result:", list_result)
print("Generator Result:", generator_result)

print("\nList Processing Time:", list_time)
print("List Peak Memory:", list_memory / (1024 * 1024), "MB")

print("\nGenerator Processing Time:", generator_time)
print("Generator Peak Memory:", generator_memory / (1024 * 1024), "MB")