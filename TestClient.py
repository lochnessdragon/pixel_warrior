import socket, sys

if __name__ == '__main__':
    data = input("What do you want to send to the server? ")
    data = bytes(data, 'utf-8') + b'\0'
    print(f"Sending: {data}")

    # send data to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5476))

    data_sent = 0
    while data_sent < len(data):
        just_sent = client.send(data[data_sent:])
        if just_sent == 0:
            print("Socket connection closed!")
            sys.exit()
        data_sent += just_sent
        print(f"Sent another: {just_sent} bytes ({(data_sent / len(data)) * 100}%)")

    # print recieved data
    print("Waiting to recieve")
    chunks = []
    bytes_recieved = 0
    while True:
        chunk = client.recv(1024)
        if chunk == b'':
            break
        chunks.append(chunk)
        bytes_recieved += len(chunk)

        print(f"Recieved another: {len(chunk)} bytes, bringing the total to: {bytes_recieved}")
        # if the message is null terminated that is the end
        if chunk[-1] == b'\0':
            break

    message = b''.join(chunks)

    print(f"Recieved: {message}")

    # close socket
    client.close()
