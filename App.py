'''
    Menu principal da Rede Social
'''

import datetime
from Model.Usuario import Usuario
from Model.Comentario import Comentario
from Database.UsuarioDAO import UsuarioDAO
from Database.ComentarioDAO import ComentarioDAO

#Função para exibir o menu da Rede Social
def exibirMenuPrincipal():

    print("==========  MENU  ==========\n"
        "1 - Criar usuário\n"
        "2 - Alterar usuário\n"
        "3 - Deletar usuário\n"
        "4 - Listar usuários\n"
        "5 - Fazer comentário\n"
        "6 - Listar comentários\n"
        "0 - Sair\n")

    try:
        opcao = int(input("Digite a opção: "))

        return opcao

    except ValueError:
        print("Opção inválida")

#Função para criar usuário
def criarUsuario():
    try:
        nome = str(input("Digite seu nome: "))
        email = str(input("Digite seu email: "))
        senha = str(input("Digite sua senha: "))
        dia = int(input("Digite seu dia de nascimento: "))
        mes = int(input("Digite seu mês de nascimento: "))
        ano = int(input("Digite seu ano de nascimento: "))
        data_nasc = datetime.date(ano, mes, dia)
        genero = str(input("Digite seu gênero: "))
        profissao = str(input("Digite sua profissão: "))
        cidade = str(input("Digite seu cidade: "))
        estado = str(input("Digite seu estado: "))
        pais = str(input("Digite seu país: "))
        usuario = Usuario(senha, email, nome, data_nasc, genero, profissao, cidade, estado, pais)
        usuarioDAO = UsuarioDAO()
        usuarioDAO.inserir(usuario)
        print("Usuário Criado!")

    except:
        print("Ocorreu um erro!")

#Função para alterar Usuário
def alterarUsuario():
    try:
        id = int(input("Digite seu id: "))
        novoNome = str(input("Digite seu nome: "))
        novoEmail = str(input("Digite seu email: "))
        novoSenha = str(input("Digite sua senha: "))
        dia = int(input("Digite seu dia de nascimento: "))
        mes = int(input("Digite seu mês de nascimento: "))
        ano = int(input("Digite seu ano de nascimento: "))
        novoData_nasc = datetime.date(ano, mes, dia)
        novoGenero = str(input("Digite seu gênero: "))
        novoProfissao = str(input("Digite sua profissão: "))
        novoCidade = str(input("Digite seu cidade: "))
        novoEstado = str(input("Digite seu estado: "))
        novoPais = str(input("Digite seu país: "))
        usuarioDAO = UsuarioDAO()
        usuarioDAO.atualizar(id, novoSenha, novoEmail, novoNome, novoData_nasc, novoGenero, novoProfissao, novoCidade, novoEstado, novoPais)
        print("Usuário Alterado!")

    except:
        print("Ocorreu um erro!")

#Função para deletar usuário
def deletarUsuario():
    try:
        id = int(input("Digite seu id: "))
        usuarioDAO = UsuarioDAO()
        usuarioDAO.deletar(id)
        print("Usuário deletado!")

    except:
        print("Ocorreu um erro!")

#Função para listar usuários
def listarUsuario():
    try:
        usuarioDAO = UsuarioDAO()
        print(usuarioDAO.listar())

    except:
        print("Ocorreu um erro!")

#Função para inserir Comentário
def inserirComentario():
    try:
        mensagem = input("Digite sua mensagem: ")
        comentario = Comentario(mensagem)
        comentarioDAO = ComentarioDAO()
        comentarioDAO.inserir(comentario)
        print("Comentário inserido!")

    except:
        print("Ocorreu um erro!")

#Função para listar comentários
def listarComentarios():
    try:
        comentarioDAO = ComentarioDAO()
        print(comentarioDAO.listar())

    except:
        print("Ocorreu um erro!")

#Função principal da Rede
def main(Args=[]):

    cont = True

    print("==========   Bem vindo a nossa Rede Social!   ==========\n")

    while(cont):

        #Exibindo Menu
        op = exibirMenuPrincipal()

        if (op == 1):
            #Criando Usuário
            criarUsuario()

        elif (op == 2):
            #alterando usuário
            alterarUsuario()

        elif (op == 3):
            #Deletando usuário
            deletarUsuario()

        elif(op == 4):
            #Listando usuários
            listarUsuario()

        elif (op == 5):
            #Inserindo Comentários
            inserirComentario()

        elif (op == 6):
            #Listando Comentários
            listarComentarios()

        elif (op == 0):
            #Saindo
            print("Saindo...")
            cont = False

        else:
            print("Opção inválida")

if (__name__== '__main__'):
    main()
