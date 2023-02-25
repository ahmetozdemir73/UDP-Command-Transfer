from UDP_transfer import UDPServer
import json
import time


with open('conf.json', 'r') as file:
    f = json.load(file)
host = f['receiver_ip']


udp = UDPServer(host=host, port=5000)


# Continuously receive data
while True:
    data = udp.receive_data()
    #print(data)
