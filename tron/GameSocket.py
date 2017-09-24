import json
import socket
import threading


class GameSocket:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, position, direction):
        data = json.dumps((position, direction))
        self.sock.send(data)

    def listen(self, callback):
        while True:
            received = self.sock.recv(1024)
            callback(received)

    def subscribe(self, callback):
        thread = threading.Thread(target=self.listen, args=(callback,))
        thread.start()
