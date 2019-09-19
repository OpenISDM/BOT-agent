import socket

 

msgFromClient       = "6;7;1.2;2;3"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("140.109.22.130", 20001)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

import time

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 

# msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 

# msg = "Message from Server {}".format(msgFromServer[0])

# print(msg)