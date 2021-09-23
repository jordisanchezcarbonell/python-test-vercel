from http.server import BaseHTTPRequestHandler
from cowpy import cow
import requests
import time
i=0
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function QWEWQQWEQWQW!')
      
        self.wfile.write(message.encode())
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

        while True:
        test2= "despues del while"
        self.wfile.write(test2.encode())

        self.wfile.write(crypto(i))
        time.sleep(15) 
        i+= 1  








def crypto(i):
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc")
    result =response.json() 
    print("ESTA ES-->",i)
    print(result[0]['id'])

 
       
i=0


