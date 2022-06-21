import socket
from gamestate import GameState
import threading

# Cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind no endereco e porta
server_address = ('localhost', 5000)
sock.bind(server_address)

# Fica ouvindo por conexoes
sock.listen(1)
arrayConnections = []
numJogadores = 0
cont = 0
running = True

while running:
    print('Aguardando a conexao dos jogadores')
    while numJogadores < 2:
        numJogadores += 1
        connection, client_address = sock.accept()
        arrayConnections.append(connection)
        print(f"Jogador nº{numJogadores} conectado")
        

    try:
        print('Jogadores conectados, vamos iniciar o jogo! :)')

        # Cria um tabuleiro de jogo vazio
        board = GameState()

        # Processa em loop
        while True:
            # Envia o tabuleiro para o jogador
            enviar = board.save()+';'+ str(cont%2)
            try:
                arrayConnections[cont%2].sendall(enviar.encode('utf-8'))
            except:
                print('Jogo encerrado!')
                input('------Pressione enter para encerrar o servidor------')
                running = False
                break

            # Recebe a jogada do jogador
            data = arrayConnections[cont%2].recv(1024)
            print(data)

            # Checa se a conexao do jogador foi terminada
            if not data:
                print('Jogador 1 se foi. :(')
                break

            # Converte para string e restaura no tabuleiro
            board.restore(data.decode('utf-8'))
            
            if board.checkWin(cont%2):
                print('True')
                arrayConnections[cont%2].sendall('True'.encode('utf-8'))
                arrayConnections[cont%2].close()
                if cont%2 == 0:
                    arrayConnections[cont%2+1].close()
                else:
                    arrayConnections[cont%2-1].close()
                break
            else:
                arrayConnections[cont%2].sendall('False'.encode('utf-8'))
            cont += 1

    finally:
        # Clean up the connection
        arrayConnections[0].close()
        arrayConnections[1].close()
