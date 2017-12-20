'''
    Criação das DML de Comentário
'''

import sqlite3
from Model.Comentario import Comentario

class ComentarioDAO():
    #Função para inserir Comentario
    def inserir(self, comentario):
        try:
            conn = sqlite3.connect('hello_if2')
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO tb_comentario(mensagem, dataHora)
                VALUES (?,?)""", (comentario.mensagem, comentario.dataHora))

            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()

    #Função para listar comentários
    def listar(self):
        comentarios = []

        try:
            conn = sqlite3.connect('hello_if2')
            cursor = conn.cursor()

            cursor.execute("""
                SELECT * FROM tb_comentario
                """)

            for linha in cursor.fetchall():
                mensagem = linha[1]

            comentario = Comentario(mensagem)

            comentarios.append(comentario)

            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()
