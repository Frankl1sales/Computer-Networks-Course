from socket import *

serverIP = '192.168.182.212'  # IP do servidor
serverPort = 9999

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Enter your lower-case word: ')
encodedMessage = message.encode()
clientSocket.sendto(encodedMessage, (serverIP, serverPort))
print(f"Sent message: {message}")

modifiedMessage, serverIP = clientSocket.recvfrom(1500)
decodedMessage = modifiedMessage.decode()

print(f"Received message: {decodedMessage}")

clientSocket.close()

