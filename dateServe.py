import http.server
import subprocess
import socket
import time

#not much to say about this code, beside linux codes I did not add much, most of the code is from the instructor notes. 

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response ( 200 )
        self.end_headers ()
        self.wfile.write ((date:=subprocess.run("date -R",  capture_output=True,shell=True, text=True).stdout).encode())
# Socket gets an available hih port number for the server        
with socket.socket() as socket:
    socket.bind(("", 0))   
    local_ip = subprocess.run("hostname -I", capture_output=True,shell=True, text=True, encoding="utf-8").stdout    
    port_num =socket.getsockname()[1]
if __name__ == '__main__':
    server = ( '', port_num)
    httpd = http.server.HTTPServer( server, Handler )
    print("To check the content;\n 1. Open another terminal window and connect to hills\n 2. Run the command below")
    print("curl -s http://"+local_ip.strip()+":"+str(port_num))
    print("Server is running", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("")
    httpd.serve_forever()
