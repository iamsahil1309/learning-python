import asyncio

async def brew_chai(name):
    print(f"brewing {name}...")
    await asyncio.sleep(3)
    print(f"{name} is ready!!!!")

async def main():
    await asyncio.gather(
        brew_chai("masala chai"),
        brew_chai("ginger chai"),
        brew_chai("black chai"),
    )

asyncio.run(main())