#https://wooody92.github.io/os/%EB%A9%80%ED%8B%B0-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EC%99%80-%EB%A9%80%ED%8B%B0-%EC%8A%A4%EB%A0%88%EB%93%9C/

#https://docs.python.org/ko/3/library/multiprocessing.html



import asyncio
import time

async def hello_world():
   while True:
      print('Hello World????')
      await asyncio.sleep(1)
   # pass

async def hello_world2():
   while True:
      print('Hello World2????')
      await asyncio.sleep(1.5)
   

async def main():
   await asyncio.wait([
         hello_world(),
         hello_world2(),
      ])

asyncio.run(main())

# loop = asyncio.get_event_loop()


# asyncio.run(hello_world(),hello_world2())
# asyncio.run()