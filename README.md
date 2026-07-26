asyncio-udp-server-playground
=============================
<kbd>[**vscode-web-action**](https://github.com/dirkarnez/vscode-web-action/actions/workflows/vscode-web.yml)</kbd><br>

- [nicoladaniello/python-udp-server: Implementation of a simple client-server in Python](https://github.com/nicoladaniello/python-udp-server)
- https://github.com/espressif/esp-idf/tree/master/examples/protocols/sockets/scripts

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor

# A heavy, blocking CPU-bound calculation
def cpu_bound_task(number):
    return sum(i * i for i in range(number))

async def main():
    loop = asyncio.get_running_loop()
    
    # Leverage a process pool for true multi-core parallelism
    with ProcessPoolExecutor() as pool:
        # Offload jobs to the pool using the event loop
        task1 = loop.run_in_executor(pool, cpu_bound_task, 10_000_000)
        task2 = loop.run_in_executor(pool, cpu_bound_task, 20_000_000)
        
        # Await the results concurrently without blocking the async thread
        results = await asyncio.gather(task1, task2)
        print(results)

if __name__ == "__main__":
    asyncio.run(main())
```
