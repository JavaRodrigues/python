menu = """
[d] Depositar
[S] Sacar
[e] Extrator
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else: 
            print("Operação fechou! O valor informado e invalido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numeros_de_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("O valor do saque excede o limite! ")
            
        elif excedeu_saques:
            print("Número máximo de saques excedido. ")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_de_saques += 1
        
        else:
            print("O valor informado é invélido. ")
    
    elif opcao == "e":
        print("\n==========Extrato==========")
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")
    
    elif opcao == "q":
        break 

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
