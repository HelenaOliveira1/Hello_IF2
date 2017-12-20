'''
    Criaçao das tabelas da Rede Social
'''

import sqlite3

#Função para criar as tabelas do banco
def criarTabelas():
        try:
            conn = sqlite3.connect('hello_if2')
            cursor = conn.cursor()

            # Criando todas as tabelas
            cursor.execute("""
            CREATE TABLE tb_usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                senha VARCHAR(25) NOT NULL,
                email VARCHAR(50) NOT NULL,
                nome VARCHAR(70) NOT NULL,
                data_nasc DATE,
                genero VARCHAR(10),
                profissao VARCHAR(20),
                cidade VARCHAR(20),
                estado VARCHAR(20),
                pais VARCHAR(20));
                """)

            print("Tabela tb_usuario criada com sucesso.")

            cursor.execute("""
            CREATE TABLE tb_comentario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mensagem VARCHAR(150),
                dataHora DATETIME);
                """)

            print("Tabela tb_comentario criada com sucesso.")

            #Salvando..
            conn.commit()

        except Exception as err:
            print(err)
            print("Criadas com sucesso!")

        finally:
            # Desconectando...
            cursor.close()
            conn.close()

criarTabelas()
