import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stoke(item) :
    print(f"checking {item} in stock...")
    time.sleep(3)
    return f"{item} stock : 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool :
        result = await loop.run_in_executor(pool, check_stoke, "ginger tea")
        print(result)

asyncio.run(main())