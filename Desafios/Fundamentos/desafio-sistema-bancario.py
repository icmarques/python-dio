#O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque
#Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo
#TOdos os saques devem ser armazenados em uma variável e exibidos na operação de extrato

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair 

saldo = 0
limite = 500
extrato = 
numero_saques = 3

while true:
    
    