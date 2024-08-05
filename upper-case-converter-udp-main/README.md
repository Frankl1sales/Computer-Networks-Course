# Conversor de Caixa Baixa para Caixa Alta usando UDP

Este projeto demonstra uma aplicação cliente/servidor simples que usa o protocolo de transporte UDP para converter mensagens de caixa baixa para caixa alta. O cliente envia uma frase em caixa baixa para o servidor, que a converte para caixa alta e envia a resposta de volta ao cliente.

## Requisitos

- Python 3
- Duas máquinas (ou duas máquinas virtuais) na mesma rede local

## Configuração da Rede

Para testar a aplicação, você precisa de duas máquinas na mesma rede local. Você pode usar um roteador ou uma rede virtual (como Hamachi) para conectar as máquinas.

### Encontrando os Endereços IP

Para cada máquina, encontre o endereço IP com o comando:

```bash
ip a
```

Anote o endereço IP da interface de rede que está em uso (não `127.0.0.1`).

## Configuração do Servidor

1. Abra um terminal na máquina que você deseja usar como servidor.
2. Navegue até o diretório do projeto.
3. Verifique e configure o firewall:

    - **Firewall do Servidor:** Certifique-se de que o firewall no servidor permite conexões na porta usada pela aplicação. Se estiver usando `ufw` no Ubuntu, você pode permitir a porta com o comando:
    
    ```bash
    sudo ufw allow 9999/udp
    ```

    - **Firewall de Rede:** Se houver um firewall de rede ou de hardware, configure-o para permitir tráfego na porta necessária.

4. Execute o servidor com o comando:

```bash
python3 upper_case_server_UDP.py
```

Você deve ver a mensagem `Server is on!`.

### Código do Servidor

```python
from socket import *

serverIP = '192.168.182.212'  # Endereço IP do servidor
serverPort = 9999  # Porta do servidor

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))

print("Server is on!")

while 1:
    message, clientIP = serverSocket.recvfrom(1500)
    decodedMessage = message.decode()
    modifiedMessage = decodedMessage.upper()
    encodedMessage = modifiedMessage.encode()
    serverSocket.sendto(encodedMessage, clientIP)
```

## Configuração do Cliente

1. Abra um terminal na máquina que você deseja usar como cliente.
2. Navegue até o diretório do projeto.
3. Execute o cliente com o comando:

```bash
python3 upper_case_client_UDP.py
```

4. Insira uma frase em caixa baixa quando solicitado.

### Código do Cliente

```python
from socket import *

serverIP = '192.168.182.212'  # Endereço IP do servidor
serverPort = 9999  # Porta do servidor

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Enter your lower-case word: ')
encodedMessage = message.encode()
clientSocket.sendto(encodedMessage, (serverIP, serverPort))

modifiedMessage, serverIP = clientSocket.recvfrom(1500)
decodedMessage = modifiedMessage.decode()

print(decodedMessage)

clientSocket.close()
```

## Testando a Aplicação

1. Inicie o servidor na máquina designada.
2. Inicie o cliente em outra máquina.
3. Digite uma frase em caixa baixa no cliente.
4. O servidor deve responder com a frase convertida para caixa alta.

## Solução de Problemas

- **Ping entre máquinas:** Verifique se as máquinas conseguem se comunicar usando o comando `ping`:

```bash
ping [IP_do_servidor]
```

- **Endereços IP corretos:** Certifique-se de que o endereço IP do servidor no código do cliente está correto.
- **Portas abertas:** Verifique se a porta escolhida (9999) está aberta em ambas as máquinas.

## Alterações para TCP

Modifique os códigos do servidor e do cliente para usar o protocolo TCP, alterando a criação do socket e adicionando conexões adequadas.

## Autor

- Prof. Guilherme Correa
- Universidade Federal de Pelotas (UFPEL)
- Maio 2022

# Lower case to upper case converter (UDP socket)

This is a simple example of UDP sockets usage based on Kurose & Ross[^1] exercises. The client sends a lower-case message to the server, which modifies it to upper case and sends back to the client.

[^1]: [Computer Networking: A Top-Down Approach](https://www.amazon.com.br/Computer-Networking-Top-Down-Approach-7th/dp/0133594149)

## Para alunos de Redes de Computadores (UFPEL)

Os códigos correspondem a uma aplicação cliente/servidor que utiliza o protocolo de transporte UDP para transferência de mensagens. A aplicação tem a seguinte função: o usuário digita uma frase em caixa baixa na aplicação cliente, que envia uma requisição ao servidor. O servidor, ao receber a frase em caixa baixa, faz a sua conversão para caixa alta (com o método upper) e envia a frase modificada ao cliente.

Seguem as tarefas que devem ser realizadas com base nos códigos disponibilizados:

1) Execute os dois códigos, de preferência em computadores separados, na sua rede local doméstica ou em uma rede virtual. Você pode usar dois computadores físicos ou duas máquinas virtuais e o software [Hamachi](https://www.vpn.net/) para simular uma rede local. Algumas alterações poderão ser necessárias (por exemplo, substituir o 'hostname' pelo endereço IP do computador que vai rodar o código de servidor e o número de porta por um número de sua escolha, pré-combinado entre cliente e servidor).

2) Depois de testar com UDP, faça modificações no código para que a aplicação funcione com o protocolo TCP.

3) Com base nesta aplicação, crie uma nova aplicação que realize a conversão de caixa baixa para caixa alta e vice-versa. Para isso, crie um protocolo simples para indicar o tipo de mensagem que o cliente envia ao servidor (por exemplo, "CA <texto>" é uma mensagem do tipo caixa alta que deve ser convertida para caixa baixa no servidor, e "CB <texto>" é uma mensagem do tipo caixa baixa que deve ser convertida para caixa alta). O servidor deve ser capaz de identificar o tipo de mensagem, realizar a operação correta  e responder o texto convertido. Esta aplicação deve usar TCP como protocolo de transporte.
