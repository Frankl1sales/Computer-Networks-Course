# Importa todas as funções e classes do módulo socket, que fornece acesso a APIs de rede
from socket import *

# Configuração do endereço IP e porta do servidor
serverIP = '0.0.0.0'  # '0.0.0.0' permite que o servidor aceite conexões de qualquer IP
serverPort = 9999     # Porta na qual o servidor vai escutar

# Cria um socket UDP (SOCK_DGRAM) usando a família de endereços IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Associa o socket ao endereço IP e à porta especificados
serverSocket.bind((serverIP, serverPort))

# Indica que o servidor está ativo
print("Server is on!")

# Loop infinito para manter o servidor ativo e processar mensagens recebidas
while True:
    # Espera receber uma mensagem do cliente. O método recvfrom retorna os dados e o endereço do remetente
    message, clientIP = serverSocket.recvfrom(1500)
    
    # Decodifica a mensagem recebida de bytes para string e imprime-a junto com o endereço do cliente
    print(f"Received message: {message.decode()} from {clientIP}")
    decodedMessage = message.decode()
    
    # Converte a mensagem para maiúsculas
    modifiedMessage = decodedMessage.upper()
    
    # Codifica a mensagem modificada de string para bytes
    encodedMessage = modifiedMessage.encode()
    
    # Envia a mensagem codificada de volta para o cliente
    serverSocket.sendto(encodedMessage, clientIP)
    
    # Imprime a mensagem modificada que foi enviada de volta para o cliente
    print(f"Sent modified message: {modifiedMessage} to {clientIP}")

