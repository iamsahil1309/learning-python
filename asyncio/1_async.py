import asyncio

async def brew(name) :
    print(f"brewing {name}...")
    await asyncio.sleep(2)   #non blocking operation means run same time without bloating 
    print(f"finished {name} brewing.")


async def main():
    await asyncio.gather(
        brew("masala chai"),
        brew("ginger chai"),
        brew("mint chai")
    )

asyncio.run(main())