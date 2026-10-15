import asyncio
import aiohttp
import time


urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]


async def fetch(session, url):
    try:
        async with session.get(url) as response:
            print(url, "Status:", response.status)
    except Exception as e:
        print(url, "Error:", e)


async def crawler():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for url in urls:
            tasks.append(fetch(session, url))

        await asyncio.gather(*tasks)


start = time.perf_counter()

asyncio.run(crawler())

end = time.perf_counter()

print("Execution Time:", round(end - start, 2), "seconds")