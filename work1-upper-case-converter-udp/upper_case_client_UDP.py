# Importa todas as funções e classes do módulo socket, que fornece acesso a APIs de rede
from socket import *

# Define o endereço IP do servidor. Esse deve ser o IP da máquina onde o servidor está executando.
serverIP = 'xxx.yyy.zzz.vvv'

# Define a porta na qual o servidor está escutando. Certifique-se de que esta porta corresponde à configurada no servidor.
serverPort = 9999

# Cria um socket UDP (SOCK_DGRAM) usando a família de endereços IPv4 (AF_INET)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Solicita ao usuário que insira uma palavra em minúsculas
message = input('Enter your lower-case word: ')

# Codifica a mensagem de string para bytes, necessário para enviar através do socket
encodedMessage = message.encode()

# Envia a mensagem codificada para o servidor, especificando o endereço IP e a porta do servidor
clientSocket.sendto(encodedMessage, (serverIP, serverPort))
print(f"Sent message: {message}")

# Espera receber uma mensagem do servidor. O método recvfrom retorna os dados e o endereço do remetente
modifiedMessage, serverIP = clientSocket.recvfrom(1500)

# Decodifica a mensagem recebida de bytes para string
decodedMessage = modifiedMessage.decode()

# Imprime a mensagem recebida do servidor, que deve estar em maiúsculas
print(f"Received message: {decodedMessage}")

# Fecha o socket do cliente
clientSocket.close()

