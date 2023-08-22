#alteração entre float e int
    
    #preco = 10
    #print(preco)
    #>>>> 10 (como o valor é inteiro e não houve nenhuma modificação na sua estrutura, o valor impresso segue sendo no formato int)
    
    #preco = float(preco)
    #print(preco)
    #>>>> 10.0 (como foi indicado o tipo float na frente do elemento, o valor é impresso neste formato, alterando de int para float)
    
    #preco = 10/2
    #print(preco)
    #>>>> 5.0 (como foi indicado a operção de divisão, o valor é impresso é alterado de int para float)
    
    #preco = 10.30
    #print(preco)
    #>>>> 10.30
    
    #preco = int(preco)
    #print(preco)
    #>>>> 10 (como foi indicado o tipo int na frente do elemento, o valor é impresso neste formato, alterando de float para int)  
    
    #preco = 10
    #print(preco // 2)
    #>>>> 5 (como foi indicado a operção de divisão com duas barras, o valor é impresso é alterado de float para int)
    
    
    
#alteração ente números e string
    
    #preco = 10.50
    #idade = 28
    
    #print(str(preco))
    #>>>> 10.5
    
    #print(str(idade))
    #>>>> 28
    
    #texto = f"idade {idade} preco {preco}"
    #print(texto)
    #>>>> idade 28 preco 10.5
    
    #Neste caso, o indicativo de str na frente do elemento, troca de int e/ou float para str. Isso não afeta a parte visual da variável.
    
    #preco = "10.50"
    #idade = "28"
    
    #print(float(preco))
    #>>>> 10.50
    
    #print(int(idade))
    #>>>> 28
    
    #Neste caso, o indicativo de int e float na frente do elemento, troca de str para sint e/ou float. Isso nafeta o visual, pois não aparece as aspas.
    
    
    
#Para verificar o tipo de variável

    #print(type(variável))