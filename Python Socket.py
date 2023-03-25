import socket

serverIP = "172.17.29.11"
serverPORT = 6000

serveraddress = (serverIP, serverPORT)
buffersize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
message = "This is Yash Aggarwal(2022B1PS0930P)"

bytestosend = str.encode(message)

UDPClientSocket.sendto(bytestosend, serveraddress)
