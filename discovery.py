from socket import socket, AF_INET, SOCK_DGRAM
PORT = 50000
MAGIC = "fna349fn"  # to make sure we don't confuse or get confused by other programs
s = socket(AF_INET, SOCK_DGRAM)  # create UDP socket
s.bind(('', PORT))

while 1:
    data, addr = s.recvfrom(1024)  # wait for a packet
    data = data.decode()
    if data.startswith(MAGIC):
        print("got service announcement from", data[len(MAGIC):])
