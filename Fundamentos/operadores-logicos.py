#São operadores utilizados em conjunto com operadores de comparação para montar uma expressão lógica.
#Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos.
    #Ex: op_comparacao + op_logico + op_comparacao ... N ...
    #saldo = 1000
    #saque = 200
    #limite = 100
    
    #saldo >= saque
    #>>>> True
    
    #saque <= limite
    #>>>> False
    
#Operador E

 #saldo = 1000
    #saque = 200
    #limite = 100
    
    #saldo >= saque and  #saque <= limite
    #>>>> False
    
    
#Operador OU
    
    #saldo = 1000
    #saque = 200
    #limite = 100
    
    #saldo >= saque or  #saque <= limite
    #>>>> True
    
    
#Operador Negação

#contatos_emergencia = []

#not 1000 > 1500
#>>>> True

#not contatos_emergencia
#>>>> True

#not "saque 1500;"
#>>>> False

#not ""
#>>>> True


#Parenteses

#saldo = 1000
#saque = 250
#limite = 200
#conta_especial = True

#saldo >= saque and saque <= limite or conta_especial and saldo >=saque
#>>>> True

#(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#>>>> True
