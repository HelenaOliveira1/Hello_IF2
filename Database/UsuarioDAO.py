'''
    Criação das DML de Usuário
'''

import sqlite3
from Model.Usuario import Usuario

class UsuarioDAO():
    #Função para inserir Usuário
    def inserir(self, usuario):
        try:
            conn = sqlite3.connect('hello_if2')
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO tb_usuario (senha, email, nome, data_nasc, genero, profissao, cidade, estado, pais)
                VALUES (?,?,?,?,?,?,?,?,?)""",
                (usuario.senha, usuario.email, usuario.nome,  usuario.data_nasc,  usuario.genero,  usuario.profissao,  usuario.cidade,  usuario.estado,  usuario.pais))

            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()

    #Função para alterar Usuário
    def atualizar(self, id, novoSenha, novoEmail, novoNome, novoData_nasc, novoGenero, novoProfissao, novoCidade, novoEstado, novoPais):
        try:
            conn = sqlite3.connect('hello_if2')
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE tb_usuario
                SET senha=?, email=?, nome=?, data_nasc=?, genero=?, profissao=?, cidade=?, estado=?, pais=?
                WHERE id=?""", (id, novoSenha, novoEmail, novoNome, novoData_nasc, novoGenero, novoProfissao, novoCidade, novoEstado, novoPais))

            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()

    #Função para deletar Usuário
    def deletar(self, id):
        try:
            conn = sqlite3.connect('hello_if2')
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM tb_usuario WHERE id=?
                """, (id,))

            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()

    #Função para listar Usuários
    def listar(self):
        usuarios = []

        try:
            conn = sqlite3.connect('hello_if2')
            cursor = conn.cursor()

            cursor.execute("""
                SELECT * FROM tb_usuario
                """)

            for linha in cursor.fetchall():
                id = linha[0]
                senha = linha[1]
                email = linha[2]
                nome = linha[3]
                data_nasc = linha[4]
                genero = linha[5]
                profissao = linha[6]
                cidade = linha[7]
                estado = linha[8]
                pais = linha[9]
                print(id)

                usuario = Usuario(senha, email, nome, data_nasc, genero, profissao, cidade, estado, pais, id)

                usuarios.append(usuario)

            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()
            return usuarios
