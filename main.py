import mysql.connector
from mysql.connector import errorcode
from os import system as sys
from functions.sqlConnection import conexao
from functions.validaInputs import *


def entradaSaida(antigoStatus, novoStatus, cpfTitular):
    if checarConexao == True:
        consulta = cnx.cursor()  # Abre a consulta
        
        idDisponiveis = consultaCPF(cpfTitular, antigoStatus)
        if idDisponiveis == None:
            pass  # Mensagem de erro já é dada na função acima
        else:
            listaIds = idDisponiveis
            id = validaInts()
            if id not in listaIds:
                print('Número de reserva inválido')
            else:
                request = f"UPDATE Reservas SET status_reserva = '{novoStatus}' WHERE id_reserva = {id};"
                consulta.execute(request)
                cnx.commit()  # Atualiza as informações no banco
                print('Status atualizado')

            consulta.close()
            cnx.close()

    else:
        cnx  # Força reconexão ao banco de dados


def consultaCPF(cpf, statusReserva):
    consulta = cnx.cursor()  # Abre a consulta
    request = f"SELECT * FROM Reservas WHERE status_reserva = '{statusReserva}' and cpf_titular = '{cpf}';"
    consulta.execute(request)

    respostaConsulta = consulta.fetchall()  # Coloca todas as linhas da consulta em uma lista
    if not respostaConsulta:
        print('Nenhuma reserva cadastrada em seu CPF')
        return None
    else:
        tamLista = len(respostaConsulta)  # Quantidade de linhas provenientes da consulta
        listaIds = []  # Lista vazia
        for dados in respostaConsulta:
            print(dados)
            tamLista = int(tamLista) - 1
            ids = respostaConsulta[tamLista][0]
            listaIds.append(ids)  # Insere os IDs disponíveis para posterior validação
        
        consulta.close()  # Fecha a consulta
        return listaIds


def encerrar():
    cnx.close()  # Fecha conexão com o banco de dados
    exit()  # Encerra o programa
    

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
        cpf = validaCpf()
        entradaSaida('Reservado', 'Ativo', cpf)

    elif resposta == '3':
        cpf = validaCpf()
        entradaSaida('Ativo', 'Finalizado', cpf)

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
