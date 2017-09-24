import socket
import sys
import threading

class GameServer:
    def __init__(self, host, port):
        self.connection_list = []

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')

        try:
            self.s.bind((host, port))
        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        print('Socket bind complete')

    def client_thread(self, conn, addr):
        # conn.send("Welcome to the server. Type something and hit enter\n")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            self.notify_clients(conn, data)
            print("%s:%s> %s" % (addr[0], str(addr[1]), data))

        conn.close()

    def notify_clients(self, conn, data):
        for connection in self.connection_list:
            if conn != connection:
                connection.sendall(data)

    def start_server(self):
        self.s.listen(10)
        print('Socket now listening')
        while 1:
            conn, addr = self.s.accept()
            print("Connected with %s:%s\n" % (addr[0], str(addr[1])))
            self.connection_list.append(conn)
            thread = threading.Thread(target=self.client_thread, args=(conn, addr))
            thread.start()

        self.s.close()

if __name__ == "__main__":
    game_server = GameServer("localhost", 8888)
    game_server.start_server()
