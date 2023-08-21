def depositar (saldo, extrato, /):
    deposito = float(input("Valor do depósito: R$ "))
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito: 10.2f}\n"
        print("Depósito realizado")
    else:
        print("Não é possível depositar valores negativos")
    
    return saldo, extrato

def sacar (*, numero_saques, saldo, extrato):
    saque = float(input("Valor do saque: R$ "))
    if saque > 0:
        if numero_saques > 0:
            if saldo >= saque:
                if saque <= limite:
                    saldo -= saque
                    numero_saques -= 1
                    extrato += f"Saque:    R$ {saque:10.2f}\n"
                    print("Retire o valor na boca do caixa")
                else:
                    print("Saque acima do limite permitido")
            else:
                print("Não há saldo suficiente")
        else:
            print("Número de saques excedido")
    else:
        print("Não é possível sacar valores negativos")

    return numero_saques, saldo, extrato

def historico(extrato, /, *, saldo):
    print("Extrato")
    print(extrato)
    print(f"Saldo:    R$ {saldo:10.2f}")

def criar_usuario (usuarios):
    cpf = int(input("Digite o CPF do usuário (somente números): "))
    cadastrado = False
    cadastrado = [True for usuario in usuarios if usuario["cpf"] == cpf]
    if cadastrado:
        print("Usuário cadastrado")
    else:
        print("Usuário não cadastrado")
        print("É necessário cadastrar o usuário")
        print("Digite os dados do usuário")
        print()
        novo_usuario = dict()
        novo_usuario["nome"] = input("Nome: ")
        novo_usuario["data_nascimento"] = input("Data de nascimento no formato dd/mm/aaaa: ")
        novo_usuario["cpf"] = cpf
        endereco = input("Logradouro: ")
        endereco += ", " + input("Número: ")
        endereco += " - " + input("Bairro: ")
        endereco += " - " + input("Cidade: ")
        endereco += "/" + input("Sigla do Estado: ")
        novo_usuario["endereco"] = endereco
        usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso!")
    return cpf

def criar_conta_corrente (contas_correntes, usuarios):
    cpf = criar_usuario(usuarios)
    numero_conta = len(contas_correntes) + 1
    nova_conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": cpf}
    contas_correntes.append(nova_conta)
    print("Conta cadastrada com sucesso!")


menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[u] = Criar usuário
[c] = Criar conta corrente
[q] = Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 3
usuarios = list()
contas_correntes = list()

opcao = "e"
while opcao != "q":
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    
    elif opcao == "s":
        numero_saques, saldo, extrato = sacar (numero_saques=numero_saques, saldo=saldo, extrato=extrato)

    elif opcao == "e":
        historico(extrato, saldo=saldo)

    elif opcao == "u":
        criar_usuario(usuarios)
    
    elif opcao == "c":
        criar_conta_corrente(contas_correntes, usuarios)

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços!")

    else:
        print("Opção inválida!")
        print("Escolha uma opção válida!")

