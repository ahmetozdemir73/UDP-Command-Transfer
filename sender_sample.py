from UDP_transfer import UDPServer
import json
import time

with open('conf.json', 'r') as file:
    f = json.load(file)
host = f['receiver_ip']



# Initialize the UDPServer class with the target IP and port
udp = UDPServer(host=host, port=5000)

data_ = "1"
previous_time = 0
while True:
    current_time = time.perf_counter()
    if current_time - previous_time >= 0.2: #optional
            udp.send_data(data_)
