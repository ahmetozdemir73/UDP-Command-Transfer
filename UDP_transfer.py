import socket

class UDPServer:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port

    def send_data(self, data):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.sendto(data.encode(), (self.host, self.port))
                print(f"Data sent: {data}")
        except Exception as e:
            print(f"Error while sending data: {e}")

    def receive_data(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.bind((self.host, self.port))
                print("Waiting for data...")
                data, addr = s.recvfrom(1024)
                print(f"Data received: {data.decode()}")
                return data.decode()
        except Exception as e:
            print(f"Error while receiving data: {e}")