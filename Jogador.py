from socket import *
from gamestate import GameState

def main():
    host = 'localhost'
    port = 5000
    addr = (host,port)
    # Cria o socket TCP/IP
    cli = socket(AF_INET,SOCK_STREAM)
    # Conecta no mesmo endereço do servidor
    cli.connect(addr)
    cont = 0
    # Inicializa um tabuleiro no processo do cliente
    board = GameState()
    try:
        while True:
            # Recebe tabuleiro do servidor e copia no tabuleiro do cliente
            data = cli.recv(1024)
            board.restore(data.decode('utf-8'))
            aux = board.getList()
            # Salva a informação sobre qual player está jogando
            if aux[-1] == '0' or aux[-1] == '1':
                jogador = int(aux[-1])
            else:
                print(f'Você perdeu!!')
                input('------Pressione enter para encerrar o jogo------')
                cli.close()
                break
            aux.pop()
            board.setList(aux)
            # Printa o tabuleiro como está atualmente
            board.print()
            # Verifica se tem apenas uma casa livre, para então definir se o que foi digitado é a casa escolhida para ocupar ou trocar pelo vazio 
            if cont < 3:
                pos = int(input(f'Jogador #{jogador+1} selecione a posição que deseja colocar sua peça: '))
                pos-=1
                if jogador == 0:
                    board.move(pos, 'blue')
                else:
                    board.move(pos, 'green')
            else:
                pos = int(input('Empate até agora, qual posição deseja trocar pelo espaço vazio: '))
                pos -= 1
                board.trocaVazio(pos)

            # Envia o tabuleiro de volta para o servidor
            cli.send(board.save().encode('utf-8'))

            # Recebe o bool que indica que há um vencedor na partida, caso haja, encerra o processo
            data2 = cli.recv(1024).decode('utf-8')
            if data2 == 'True':
                print(f'Você venceu!!')
                input('------Pressione enter para encerrar o jogo------')
                cli.close()
                break
            cont+=1
    finally:
        cli.close()

main()

