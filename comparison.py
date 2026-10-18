import time 
from typing import List

# modern way to work with threads - thread management 
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor


# simulates io-bounded tasks - api requests <--- use threading
def do_work(task_id: int, duration: float = 0.1) -> str:
    time.sleep(duration)
    return f"Task {task_id} completed"


def run_threading(tasks: int = 5, max_workers: int = 5) -> List[str]:
    results: List[str] = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_work, i, 0.1) for i in range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    return results


# use multi-processing for cpu-bound task
def do_cpu_work(task_id: int, iterations: int = 1000000) -> str:
    result = 0 
    for i in range(iterations):
        result += i * i 
    return f"Task {task_id} compelted (result = {result})"

def run_multiprocessing(tasks: int = 5, max_workers: int = 5) -> List[str]:
    results: List[str] = [] 
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_cpu_work, i, 1000000) for i in range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    
    return results




# def run_sync(tasks: int = 5) -> List[str]:
#     results: List[str] = []
#     for i in range(tasks):
#         result = do_work(i, duration=0.1)
#         results.append(result)

#     return results

# https://www.indently.io/



if __name__ == "__main__":
    start = time.perf_counter()
    results = run_multiprocessing(tasks=5)
    elapsed = time.perf_counter() - start


    print("Multiprocessing result")
    for result in results:
        print(f"{result}")


    print(f"\nTotal time: {elapsed:.2f} seconds")
    # print("Note: Tasks ran one after another (synchronous execution)")
    # print("Note: Tasks run concurrently using threads (I/O-bound tasks)")
    # each process has its own GIL
    print("Note: Tasks ran in parallel using separate processes (CPU-bound tasks)")




# Reference
# https://www.youtube.com/watch?v=QlkXji08lno - Indently
# https://www.youtube.com/watch?v=tSLDcRkgTsY&pp=ygUZYXN5bmMgaW8gIHB5dGhvbiBwcmFjdGljZQ%3D%3D