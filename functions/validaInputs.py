def validaNome():
    nome = input('Nome: ')  # Apenas o primeiro nome
    while nome.isalpha() == False:  # alphanumeric function
        nome = input('Nome: ')
    else:
        return nome


def validaCpf():
    cpf = input('CPF: ')
    while cpf.isdigit() == False or len(cpf) != 11:
        cpf = input('CPF: ')
    else:
        return cpf


def validaNrPessoas():
    nrPessoas = input('Número de pessoas: ')
    while nrPessoas.isdigit() == False or int(nrPessoas) > 5:  # Máx 5
        nrPessoas = input('Número de pessoas: ')
    else:
        return int(nrPessoas)


def validaTipoQuarto():
    print('S - Standard [100p/pessoa p/diaria]\n'
        'D - Deluxe [300p/pessoa p/diaria]\n'
        'P - Premium [200p/pessoa p/diaria]'
    )

    resposta = ('S', 'D', 'P', 'STANDARD', 'DELUXE', 'PREMIUM')
    opcao = input('> ').upper()  # Capslock

    while opcao not in resposta:
        opcao = input('> ').upper()  # loop

    # Validadores
    if opcao == resposta[0] or opcao == resposta[3]:  # Standard
        opcao = 'S'
        return opcao

    elif opcao == resposta[1] or opcao == resposta[4]:  # Deluxe
        opcao = 'D'
        return opcao

    elif opcao == resposta[2] or opcao == resposta[5]:  # Premium
        opcao = 'P'
        return opcao
    

def validaDiarias():
    diarias = input('Diárias: ')
    while diarias.isdigit() == False or int(diarias) > 15:  # Máx 15
        diarias = input('Diárias: ')
    else:
        return int(diarias)


def validaValorReserva(func1, func2, func3):  # validaNrPessoas, validaTipoQuarto, validaDiarias
    if func2 == 'S':
        func2 = 100
    elif func2 == 'D':
        func2 = 200
    elif func2 == 'P':
        func2 = 300
    
    total = func1 * func2 * func3
    return total


def validaInts():
    num = input('ID: ')
    while num.isdigit() == False:
        num = input('ID: ')
    else:
        return int(num)
