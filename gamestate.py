import numpy as np
from random import *

class GameState:
    """
    Classe que representa o estado do jogo.
    """

    # -------------------------------------------------
    def __init__(self):
        """
        Construtor. Initializa o tabuleiro com 7 espaços vazios.
        """
        self.board = list("-/-/-/-/-/-/-".split("/"))
        self.jogador = 0

    # -------------------------------------------------
    def save(self):
        """
        Salva os dados do tabuleiro para uma string.

        Gera uma string com as peças do tabuleiro separadas por
        ponto-e-vírgula (';'), de forma que o estado do jogo possa
        ser comunicado via socket.

        Retorno
        ----------
        data: str
            String de texto com os dados do tabuleiro separados por
            ponto-e-vírgula (';'), prontos para serem comunicados.     
        """
        return ';'.join([str(x) for x in self.board])

    # -------------------------------------------------
    def restore(self, data):
        """
        Restaura os dados do tabuleiro a partir de uma string.

        Lê uma string com as peças do tabuleiro separadas por
        ponto-e-vírgula (';'), de forma que o estado do jogo possa ser
        comunicado via socket.

        Parâmetros
        ----------
        data: str
            String de texto com os dados do tabuleiro separados por um
            ponto-e-vírgula (';'), prontos para serem atualizados neste
            objeto.
        """
        self.board = data.split(';')

    # -------------------------------------------------
    def move(self, pos, color):
        """
        Faz uma jogada no tabuleiro, nas posições dadas.

        Parâmetros
        ----------
        pos: int
            Número da posição que peça será inserida no tabuleiro no tabuleiro, no intervalo [0,2].
        color: str
            Palavra com a cor da peça a ser inserida na posição, entre as opções 'blue' e 'green'.        
        """

        # Valida os parâmetros de entrada
        if pos < 0 or pos > 6:
            raise RuntimeError('Posição inválida: {}'.format(pos))
        color = color.lower()
        if color != 'blue' and color != 'green':
            raise RuntimeError('Jogada inválida: {}'.format(piece))

        # Verifica se a posição jogada está vazia
        if self.board[pos] != '-':
            raise RuntimeError('Posição já preenchida: {}'.format(pos))

        # Faz a jogada
        if color == 'blue':
            color = 1
        else:
            color = 2
        self.board[pos] = color
    # -------------------------------------------------
    def getList(self):
        """
        Retorna a lista presente na instância da classe.

        Retorno
        ----------
        self.board: list
            Lista com as casas do tabuleiro.
        """
        return self.board
    # -------------------------------------------------
    def setList(self,lista):
        """
        Transforma a lista atual da instância em outra
        passada como parâmetro

        Parâmetros
        ----------
        lista: list
            Lista a ser inserida no local do self.board
            na atual instância.
        """
        self.board = lista
    # -------------------------------------------------
    def print(self):
        print(f'           1:({self.board[0]})      ')
        print(f'   2:({self.board[1]})---3:({self.board[2]})---4:({self.board[3]})')
        print(f'5:({self.board[4]})------6:({self.board[5]})------7:({self.board[6]})')
    # -------------------------------------------------
    def trocaVazio(self,pos):
        posic = 0
        cont = 0
        for i in self.board:
            cont += 1
            if i == '-':
                posic = cont-1
        self.board[posic] = self.board[pos]
        self.board[pos] = '-'
    # -------------------------------------------------
    def checkWin(self,jogador):
        if self.board[0] == self.board[1] and self.board[1] == self.board[4]:
            if self.board[0] == '-':
                return False
            return True
        elif self.board[0] == self.board[2] and self.board[2] == self.board[5]:
            if self.board[0] == '-':
                return False
            return True
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            if self.board[0] == '-':
                return False
            return True
        elif self.board[1] == self.board[2] and self.board[2] == self.board[3]:
            if self.board[1] == '-':
                return False
            return True
        elif self.board[4] == self.board[5] and self.board[5] == self.board[6]:
            if self.board[4] == '-':
                return False
            return True
        return False


