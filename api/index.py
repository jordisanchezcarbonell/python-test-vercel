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
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())

        while True:
            
        self.wfile.write(crypto(i))
        time.sleep(15) 
        i+= 1  








def crypto(i):
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc")
    result =response.json() 
    print("ESTA ES-->",i)
    print(result[0]['id'])

 
       
i=0


