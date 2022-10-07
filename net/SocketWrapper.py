import socket


class SocketWrapper():

    def __init__(self, sock=None):
        if sock is None:
            # create a new socket
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self._socket = sock

    def connect(self, host, port):
        self._socket.connect((host, port))

    def write(self, msg):
        total_bytes = 0
        while total_bytes < len(msg):
            bytes_sent = self._socket.send(msg[total_bytes:])
            if bytes_sent == 0:
                raise RuntimeError("socket connection broken")
            total_bytes += bytes_sent

    def read(self):
        data = []
        bytes_recieved = 0
        while True:
            chunk = self._socket.recv(1024)
            if chunk == b'':
                # connection closed
                raise RuntimeError("socket connection broken")
            data.append(chunk)
            bytes_recieved = bytes_recieved + len(chunk)

            # if the message is null terminated, that is the end
            print(chunk[-1])
            if chunk[-1] == 0:
                break

        data = b''.join(data)
