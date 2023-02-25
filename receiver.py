from UDP_transfer import UDPServer
import RPi.GPIO as GPIO
import json
import time


with open('conf.json', 'r') as file:
    f = json.load(file)
host = f['receiver_ip']
target_pin = f['write_pin']

udp = UDPServer(host=host, port=5000)

GPIO.setmode(GPIO.BCM)
GPIO.setup(target_pin, GPIO.OUT)

# Continuously receive data
while True:
    GPIO.output(target_pin,0)
    data = udp.receive_data()
    if data == "1":
        GPIO.output(target_pin,1)
        print("GPIO", target_pin, "pin is activated")
        time.sleep(0.2)
