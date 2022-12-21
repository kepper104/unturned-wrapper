import main2
import time
import asyncio

# a = main2.Interactor()

async def init(i):
    await i.start()

async def send_input():
    i = main2.Interactor()
    print('crated')
    await init(i)
    print("enter")
    # i = await init()
    print('start wait')
    time.sleep(5)
    await i.send()
    print('sent')

asyncio.run(send_input())