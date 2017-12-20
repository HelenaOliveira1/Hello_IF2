'''
    Criação da classe Comentário
'''

import datetime

class Comentario():
    #Definindo o construtor
    def __init__(self, mensagem):
        self.mensagem = mensagem
        self.dataHora = datetime.datetime.now()
