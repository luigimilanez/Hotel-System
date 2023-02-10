import mysql.connector
from mysql.connector import errorcode
from os import system as sys
from functions.sqlConnection import conexao
from functions.validaInputs import *


def inserirAlterar(escolha):  # Cadastrar / Alterar
    if checarConexao == True:
        consulta = cnx.cursor()  # Abre a consulta

        if escolha == 'Cadastrar':  # Não pedirá esses dados caso for alterar os dados da reserva
            statusReserva = 'Reservado'
            nome = validaNome()
            cpf = validaCpf()           
            nrPessoas = validaNrPessoas()
            tipoQuarto = validaTipoQuarto()
            diarias = validaDiarias()
            valorReserva = validaValorReserva(nrPessoas, tipoQuarto, diarias)

            request = 'INSERT INTO Reservas (status_reserva, nm_titular, cpf_titular, nr_pessoas, tp_quarto, diarias, valor_reserva) VALUES (%s, %s, %s, %s, %s, %s, %s);'  # Comando
            valores = (statusReserva, nome, cpf, nrPessoas, tipoQuarto, diarias, valorReserva)
            consulta.execute(request, valores)
            cnx.commit()
            print('Reserva cadastrada')


        elif escolha == 'Alterar':
            cpf = validaCpf()
            idDisponiveis = consultaCPF(cpf, 'Reservado')
            if idDisponiveis == None:
                pass  # Mensagem de erro é dada pela função
            else:
                listaIds = idDisponiveis
                print('Digite o ID da reserva a ser alterada')
                id = validaInts()
                if id not in listaIds:
                    print('Número de reserva inválido')
                else:
                    nrPessoas = validaNrPessoas()
                    tipoQuarto = validaTipoQuarto()
                    diarias = validaDiarias()
                    valorReserva = validaValorReserva(nrPessoas, tipoQuarto, diarias)

                    request = f"UPDATE Reservas SET nr_pessoas = {nrPessoas}, tp_quarto = '{tipoQuarto}', diarias = {diarias}, valor_reserva = {valorReserva} WHERE id_reserva = {id};"
                    consulta.execute(request)
                    cnx.commit()
                    print('Dados atualizados')
        
        consulta.close()
        cnx.close()

    else:
        cnx  # Força reconexão com o banco de dados


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
        cnx  # Força reconexão com o banco
        

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


def relatorio(statusReserva):
    def consultaDados():
        filtro = []
        for dados in consulta:
            filtro.append(dados)
            print(dados)
        if not filtro:
            return print(f'Não há reservas com o status "{statusReserva}"')

    if checarConexao == True:
        consulta = cnx.cursor()  # Abre a consulta
        statusBanco = ['Reservado', 'Ativo', 'Finalizado']

        if statusReserva == 'CPF':
            cpf = validaCpf()

            print('1 - Reservado\n'
            '2 - Ativo\n'
            '3 - Finalizado\n'
            '4 - Menu\n')

            option = input('Opção ')

            if option == '1':
                consultaCPF(cpf, 'Reservado')
            elif option == '2':
                consultaCPF(cpf, 'Ativo')
            elif option == '3':
                consultaCPF(cpf, 'Finalizado')
            elif option == '4':
                pass  # Volta para o menu
            else:
                pass  # Volta para o menu

        elif statusReserva in statusBanco:
            request = f"SELECT * FROM Reservas WHERE status_reserva = '{statusReserva}';"
            consulta.execute(request)
            consultaDados()

        else:
            request = f"SELECT * FROM Reservas;"
            consulta.execute(request)
            consultaDados()

        consulta.close()
        cnx.close()

    else:
        cnx  # Força reconexão com o banco de dados


def encerrar():
    cnx.close()  # Fecha conexão com o banco de dados
    exit()  # Encerra o programa
    
    
sys('cls')  # Limpa o terminal
while True:
    cnx = conexao('cnx')  # Abre a conexão com o banco de dados
    checarConexao = cnx.is_connected()  # True se conectado

    print('\n'
        '1 - Cadastrar Reserva\n'
        '2 - Entrada do Cliente (Check In)\n'
        '3 - Saída do Cliente (Check Out)\n'
        '4 - Modificar Reservas\n'
        '5 - Relatórios\n'
        '6 - Sair\n'
    )

    resposta = input('> ')

    if resposta == '1':
        inserirAlterar('Cadastrar')

    elif resposta == '2':
        cpf = validaCpf()
        entradaSaida('Reservado', 'Ativo', cpf)

    elif resposta == '3':
        cpf = validaCpf()
        entradaSaida('Ativo', 'Finalizado', cpf)

    elif resposta == '4':
        inserirAlterar('Alterar')
      
    elif resposta == '5':
        print(
        '1 - CPF\n'
        '2 - Todos\n'
        '3 - Reservados\n'
        '4 - Ativos\n'
        '5 - Finalizados\n'
        '6 - Voltar\n'
        )

        option = input('Opção ')

        if option == '1':
            relatorio('CPF')  # Busca por cpf

        elif option == '2':
            relatorio('Todos')  # Busca por todos os registros do banco

        elif option == '3':
            relatorio('Reservado')  # Busca pelo status Reservado

        elif option == '4':
            relatorio('Ativo')  # Busca pelo status Ativo

        elif option == '5':
            relatorio('Finalizado')  # Busca pelo status Finalizado

        elif option == '6':
            pass  # Loop - Volta para o menu principal


    elif resposta == '6':
        encerrar()  # Encerra o aplicativo

        
    else:
        pass  # Loop
