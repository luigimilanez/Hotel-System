import mysql.connector
from mysql.connector import errorcode
from os import system as sys
from functions.sqlConnection import conexao
from functions.validaInputs import *


def encerrar():
    cnx.close()  # Fecha conexão com o banco de dados
    exit()
    

while True:
    sys('cls')  # Limpa o terminal
    cnx = conexao('cnx')  # Abre a conexão com o banco de dados
    checarConexao = cnx.is_connected()  # True se conectado

    print(
        '1 - Cadastrar Reserva\n'
        '2 - Entrada do Cliente (Check In)\n'
        '3 - Saída do Cliente (Check Out)\n'
        '4 - Modificar Reservas\n'
        '5 - Relatórios\n'
        '6 - Sair'
    )

    resposta = input('> ')

    if resposta == '1':
        pass

    elif resposta == '2':
        pass

    elif resposta == '3':
        pass 

    elif resposta == '4':
        pass
      
    elif resposta == '5':
        print(
        '1 - CPF\n'
        '2 - Todos\n'
        '3 - Reservados\n'
        '4 - Ativos\n'
        '5 - Finalizados\n'
        '6 - Cancelados\n'
        '7 - Voltar'
        )

        option = input('Opção ')

        if option == '1':
            pass  # Busca por cpf

        elif option == '2':
            pass  # Busca por todos os registros do banco

        elif option == '3':
            pass  # Busca pelo status Reservado

        elif option == '4':
            pass  # Busca pelo status Ativo

        elif option == '5':
            pass  # Busca pelo status Finalizado

        elif option == '6':
            pass  # Busca pelo status Cancelado

        elif option == '7':
            pass  # Loop - Volta para o menu principal


    elif resposta == '6':
        encerrar()  # Encerra o aplicativo

        
    else:
        pass  # Loop
