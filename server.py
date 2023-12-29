
import websockets
import asyncio
from timeit import default_timer as timer

PORT = 8000

async def echo(websocket):
      print("A client just connected")
  
      #Throughput
      count = 0
      sec = 0

      dat1 = open("C:/Users/Ömer Alp/Desktop/1.5mb.txt", "r")
      dat2 = open("C:/Users/Ömer Alp/Desktop/1.1mb.txt", "r")
      dat3 = open("C:/Users/Ömer Alp/Desktop/100kb.txt", "r")
      dat4 = open("C:/Users/Ömer Alp/Desktop/1mb.txt", "r")
      dat5 = "Pong: Game"
      dat6 = open("C:/Users/Ömer Alp/Desktop/1kb.txt", "r")

      
      cont = dat3.read()

      start1 = timer()
      while (sec) < 1.000000: 
       await websocket.send(cont)
       end = timer()
       count = count + 1
       print("Done!")
       sec = end - start1
       start = timer()
      
      print("Time: " + str(round(sec,3)) + " second. "+ "Throughput: " + str(round(count/sec)) + " pps(Packets per second)") 
      await websocket.send("#")

async def main():
  async with await websockets.serve(echo, "localhost", PORT):
    print("Asyncio server listening on port: " + str(PORT))
    await asyncio.Future()
  
  
asyncio.run(main())