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

#### Passos Detalhados:

1. **Execute o comando:**
   ```bash
   ip a
   ```

2. **Procure a interface de rede ativa:**
   - No exemplo fornecido, a interface de rede `wlp12s0` está ativa (`state UP`).
   - A interface ativa normalmente tem a descrição `BROADCAST,MULTICAST,UP,LOWER_UP`.

3. **Encontre o endereço IP:**
   - Sob a interface `wlp12s0`, procure a linha que começa com `inet`.
   - O endereço IP está listado após `inet`. No exemplo, o endereço IP é `xxx.yyy.zzz.vvv`.

Resumindo, o endereço IP do servidor no exemplo é `xxx.yyy.zzz.vvv`, que pode ser encontrado na linha:
```plaintext
inet xxx.yyy.zzz.vvv/24 brd xxx.yyy.zzz.255 scope global dynamic noprefixroute wlp12s0
```

Configuração do Servidor

    Abra um terminal na máquina que você deseja usar como servidor.

    Navegue até o diretório do projeto.

    Verifique e configure o firewall:
        Firewall do Servidor: Certifique-se de que o firewall no servidor permite conexões na porta usada pela aplicação. Se estiver usando ufw no Ubuntu, você pode permitir a porta com o comando:

    bash

sudo ufw allow 9999/udp

    Firewall de Rede: Se houver um firewall de rede ou de hardware, configure-o para permitir tráfego na porta necessária.

Teste Localmente:

Verifique se o servidor e o cliente estão na mesma rede e se o servidor pode se comunicar com ele mesmo. Tente usar o comando netcat (ou nc) para testar a comunicação na mesma porta:

No Servidor:

bash

nc -ul 9999

No Cliente:

bash

echo "test message" | nc -u xxx.yyy.zzz.vvv 9999

Execute o servidor com o comando:

bash

python3 upper_case_server_UDP.py

Você deve ver a mensagem Server is on!.

### Código do Servidor

```python
serverIP = '0.0.0.0'  # Aceita conexões de qualquer IP
serverPort = 9999  # Porta do servidor
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

serverIP = 'xxx.yyy.zzz.vvv'  # Endereço IP do servidor
serverPort = 9999  # Porta do servidor
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
