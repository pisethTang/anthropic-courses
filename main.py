import time 
import asyncio


# def i_am_synchronous() -> None:
#     print("Hello from the synchronous function")
#     time.sleep(2)
#     print("Finished downloading file!")

# Tasks can yield control, therefore ... 
# Execution can be non-blocking, therefore ...
# we can be more efficient.

# Concurrency vs parallelism

# Problem solved with async 
# io-bounded tasks: limited by a blocking i/o substem such as network requests, file operations, db queries, etc. -- good use cases for async
# cpu-bounded tasks: limited by the speed of your cpu: heavy computations, 3d rendering, and img/vid processing. -- can be solved by multi-processing, multi-threading, architectural decision to split workload and aggregate results. 


# i_am_synchronous()




# first, we have to learn the syntax (still single-threaded)
# async def - defines a coroutine function (a function that yields control)
# await - pauses execution until awaitable completes.
# event loop - the "heart" of async execution. 


# def do_groceries():
#     pass 

# async def boil_water():         # await boiling_water()
#     pass 


# async def blend_strawberries(): # await blend_strawberries()
#     pass 

# async def cook_pasta():
#     pass 


# async def add_straw_berries():
#     pass 


# async def enjoy_meal():
#     pass 


# event loop (single-threaded) - tasks scheduler  

async def fetch(delay: int, name: str) -> str:
    print(f"STarting to fetch {name} ...")
    await asyncio.sleep(delay)

    print(f"Finished fetching {name}!")
    return f"Data from {name}"


# asyncio.run(main()) # 


# Reference
# https://www.youtube.com/watch?v=-SLws9PJFkI