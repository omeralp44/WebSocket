import tornado.ioloop
import tornado.websocket
from timeit import default_timer as timer
import asyncio

async def main():

        url = "ws://localhost:8000/ws"
        
        start4 = timer()
        ws = await tornado.websocket.websocket_connect(url)
        end4 = timer()
        print("Connection established!")

        t4 = (end4-start4)*1000
        
      # Latency
        count = 0      
        tot = 0
        msg = "Game"

        await ws.write_message(msg)
   
        while msg != "#": 

            start = timer()
            msg = await ws.read_message()
            end = timer()
            t = (end-start)*1000
            #print(msg)
      
            if msg != "#":
                count = count + 1
                tot = tot + t
                print("Latency: " + str(round(t,2)) + " ms")
      
        av = tot / count
        print("Connection establishment time: " + str(round(t4,2)) + " ms.")
        print("Average latency: " + str(round(av,2)) + " ms." + " Packets:" + str(count))   

#asyncio.run(main())
if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
