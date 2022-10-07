import socket
import threading

def client_code(client):
    # try to recieve data
    print("Attempting to recieve the data!")
    data = []
    bytes_recieved = 0
    while True:
        chunk = client.recv(1024)
        if chunk == b'':
            # connection closed
            client.close()
            return
        data.append(chunk)
        bytes_recieved = bytes_recieved + len(chunk)
        print(f"Recieved another: {len(chunk)} bytes, bringing the total to: {bytes_recieved}")
        # if the message is null terminated, that is the end
        print(chunk[-1])
        if chunk[-1] == 0:
            break

    data = b''.join(data)

    print(data)

    # try to send data
    if len(data) > 0:
        # send the data back
        print("Sending data back!")
        data_sent = 0
        while data_sent < len(data):
            just_sent = client.send(data[data_sent:])
            if just_sent == 0:
                print("Socket connection closed!")
                client.close()
                return
            data_sent += just_sent
            print(f"Sent another: {just_sent} bytes ({data_sent / len(data) * 100}%)")

    print("Closing socket!")

    # close the socket
    client.close()

class Server:
    def __init__(self, port, max_conn):
        self.port = port
        self.max_conn = max_conn
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to a public name on the required port socket.gethostname()
        self._socket.bind(("localhost", self.port))

        # become a server socket
        self._socket.listen(self.max_conn)

        # created empty list for connected clients
        self.clients = []

    def update(self):
        (client, address) = self._socket.accept()

        # do something with the client socket
        print("Client accepted, starting thread!")
        client_thread = threading.Thread(target=client_code, args=(client,))
        client_thread.start()
        self.clients.append(client_thread)

    def shutdown(self):
        for thread in self.clients:
            thread.join()
        self._socket.close()

if __name__ == '__main__':
    print("Setting up echo server...")
    host = Server(5476, 5)

    print(f"Listening on localhost:{host.port}")

    while True:
        host.update()

    host.shutdown()
