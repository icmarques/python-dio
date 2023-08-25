#variáveis: são os valores que podem sofrer alterações no decorrer da execução do programa.
novo_saldo = str("Saldo (R$): ")
saldo = float(1500)
print(str(novo_saldo), float(saldo))


operacao = input (str("Qual o tipo de operação que será feita?\nEscolha entre:'Depósito' ou 'Saque'\n\nDigite aqui a operação desejada: "))
print(operacao)
    
if operacao == str("Depósito"):
    valor_saque = float(0)
    valor_deposito = input ("Digite o valor a ser depostitado (R$): ")
    print(valor_deposito)

if operacao == str("Saque"):
    valor_deposito = float(0)
    valor_saque = input ("Digite o valor a ser sacado (R$): ")
    print(valor_saque)
 
if valor_deposito != float(0):
    saldo_atual_deposito = float(saldo) + float(valor_deposito)
    print(str("Saldo atual (R$): "), float(saldo_atual_deposito))

if valor_saque != (0):    
    saldo_atual_saque = float(saldo) - float(valor_saque)
    print(str("Saldo atual (R$): "), float(saldo_atual_saque))






 










