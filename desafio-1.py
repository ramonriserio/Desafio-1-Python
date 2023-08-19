menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 3

opcao = "e"
while opcao != "q":
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Valor do depósito: R$ "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito: 10.2f}\n"
            print("Depósito realizado")
        else:
            print("Não é possível depositar valores negativos")
    
    elif opcao == "s":
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
    
    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Saldo:    R$ {saldo:10.2f}")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços!")

    else:
        print("Opção inválida!")
        print("Escolha uma opção válida!")

