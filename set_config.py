import json

class Config:
    def __init__(self, filename):
        self.filename = filename
        self.config = None
        self.load()

    def load(self):
        with open(self.filename, 'r') as file:
            self.config = json.load(file)

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.config, file)

    def update_receiver_ip(self, receiver_ip):
        self.config['receiver_ip'] = receiver_ip
        self.save()