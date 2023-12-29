
import websockets
import asyncio
from timeit import default_timer as timer

async def listen():
  
  url = "ws://localhost:8000/ws"

  start4 = timer()
  async with websockets.connect(url) as ws:
   print("Connection established!")
   end4 = timer()
   t4 = (end4-start4)*1000

#  Latency
   count = 0      
   tot = 0
   msg = "Game"
      
   await ws.send(msg)
   
   while msg != "#": 

      start = timer()
      msg = await ws.recv()
      end = timer()
      t = (end-start)*1000  # + send_time
      #print(msg)
      
      if msg != "#":
         count = count + 1
         tot = tot + t
         print("Latency: " + str(round(t,2)) + " ms")
      
   av = tot / count
   print("Connection establishment time: " + str(round(t4,2)) + " ms.")
   print("Average latency: " + str(round(av,2)) + " ms." + " Packets:" + str(count))   

asyncio.run(listen())