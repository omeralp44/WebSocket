import tornado.ioloop
import tornado.web
import tornado.websocket
from timeit import default_timer as timer

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    async def on_message(self, message):
        
        #Throughput
        count = 0
        sec = 0
        
        dat1 = open("C:/Users/Ömer Alp/Desktop/1.5mb.txt", "r")
        dat2 = open("C:/Users/Ömer Alp/Desktop/1.1mb.txt", "r")
        dat3 = open("C:/Users/Ömer Alp/Desktop/100kb.txt", "r")
        dat4 = open("C:/Users/Ömer Alp/Desktop/1mb.txt", "r")
        dat5 = "Pong: Game"
        dat6 = open("C:/Users/Ömer Alp/Desktop/10mb.txt", "r")
        dat7 = open("C:/Users/Ömer Alp/Desktop/11mb.txt", "r")

        
        cont = dat3.read()

        start1 = timer()
        while (sec) < 1.000000: 
          await self.write_message(cont)
          end = timer()
          count = count + 1
          print("Done!")
          sec = end - start1
          start = timer()
        
        print("Time: " + str(round(sec,3)) + " second. "+ "Throughput: " + str(round(count/sec)) + " pps(Packets per second)") 
        await self.write_message("#")
        
    def on_close(self):
       print("WebSocket closed")

def make_app():
    return tornado.web.Application([
        (r"/ws", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("Tornado server listening on port: " + str(8000))
    tornado.ioloop.IOLoop.current().start()