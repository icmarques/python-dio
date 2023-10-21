#O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque - OK
#Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será 
#possível sacar o dinheiro por falta de saldo - OK
#Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato ok

menu = """
Escolha uma opção abaixo: 

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair 

=>"""

saldo = 0
limite = 500
extrato = 0
numero_saques = 0
limite_saques = 3
extrato_deposito = 0
extrato_saque = 0


while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Opção selecionada: Depósito")
        print("Digite o valor do depósito: ")
        valor_deposito = float(input())
        saldo_atual_deposito = saldo + valor_deposito
        saldo = saldo_atual_deposito
        extrato_deposito += valor_deposito
        print(f"Seu saldo atual é: R$ {saldo}")
        
        
    elif opcao == "s":
        
        if limite_saques > 0: 
            print("Opção selecionada: Saque")
            print("Digite o valor de saque: ")
            valor_saque = float(input())
            
            if saldo < valor_saque:
                print("Operação negada: Saldo insuficiente.")
        
            elif valor_saque > float(500):
                print("Operação negada: Valor para saque é de até R$500.00")
        
            elif valor_saque <= float(500):
                saldo_atual_saque = saldo - valor_saque
                saldo = saldo_atual_saque
                operacao_saque = limite_saques - 1
                limite_saques = operacao_saque
                extrato_saque += valor_saque
                print(f"Seu saldo atual é: R$ {saldo}")
                
        elif limite_saques <= 0:
            print("Operação negada: Limite de saques diários atingidos")
            
            
    elif opcao == "e":
        print("Opção selecionada: Extrato")
        
        if extrato_deposito != 0:
            print(f"Total depósitos: R$ {extrato_deposito:.2f}")
            
        elif extrato_saque != 0:
            print(f"Total saques: R$ {extrato_saque:.2f}")
            
        
        print(f"Saldo: R$ {saldo:.2f}")
       
       
    elif opcao == "q":
        print("Obrigada pela preferência.")
        break
        
    
    else:
        print("Operação inválida. Selecione novamente a operação desejada.")
    