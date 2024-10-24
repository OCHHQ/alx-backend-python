0x01. Python - Async

1. Async and Await Syntax
async: This keyword is used to declare a function as a coroutine. A coroutine is a special kind of function that can pause and resume its execution, which is key in asynchronous programming.

Example:
async def my_coroutine():
    return "Hello, async world!"
await: This keyword is used to pause the execution of a coroutine until the result of another coroutine or asynchronous operation is ready.

Example:

python
Copy code
async def my_coroutine():
    await asyncio.sleep(1)  # Pauses the coroutine for 1 second
    print("Waited for 1 second")
2. Executing an Async Program with asyncio
asyncio is the library that provides tools for asynchronous programming in Python. To run an async program, you need an event loop. The event loop runs asynchronous tasks (coroutines) concurrently.

Example of running a coroutine:

python
Copy code
import asyncio

async def main():
    print("Async program started")
    await asyncio.sleep(1)
    print("Async program ended")

asyncio.run(main())  # Starts the event loop and runs the main coroutine
3. Running Concurrent Coroutines
In async programming, concurrency means that multiple coroutines can run seemingly at the same time, even though only one is being executed at any given moment. This is done by switching between coroutines while waiting for I/O operations.

Example:

python
Copy code
import asyncio

async def coroutine_one():
    await asyncio.sleep(2)
    print("Coroutine One Done")

async def coroutine_two():
    await asyncio.sleep(1)
    print("Coroutine Two Done")

async def main():
    await asyncio.gather(coroutine_one(), coroutine_two())  # Runs both coroutines concurrently

asyncio.run(main())
Output:

python
Copy code
Coroutine Two Done
Coroutine One Done
4. Creating asyncio Tasks
asyncio.create_task() allows you to create tasks that will run concurrently. This is useful if you want to schedule several coroutines to run without blocking each other.

Example:

python
Copy code
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

async def say_goodbye():
    await asyncio.sleep(2)
    print("Goodbye")

async def main():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_goodbye())
    
    await task1
    await task2

asyncio.run(main())
5. Using the random Module
random.uniform(a, b) generates a random float between a and b. You can use it when simulating random delays or time intervals in your async tasks.

Example:

python
Copy code
import asyncio
import random

async def random_sleep():
    delay = random.uniform(1, 3)
    await asyncio.sleep(delay)
    print(f"Slept for {delay:.2f} seconds")

asyncio.run(random_sleep())
