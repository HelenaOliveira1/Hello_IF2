'''
    Criação da classe Usuario
'''

class Usuario():
    #Definindo o construtor
    def __init__(self, senha, email, nome, data_nasc, genero, profissao, cidade, estado, pais, id=None):
        self.senha = senha
        self.email = email
        self.nome = nome
        self.data_nasc = data_nasc
        self.genero = genero
        self.profissao = profissao
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    #Alterando o método __str__ de Usuário
    def __str__(self):
        return "Usuario <%s>" % (self.nome)

    #Alterando o método representativo de Usuário
    def __repr__(self):
        return self.__str__()
