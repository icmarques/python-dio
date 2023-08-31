#Métodos úteis para manipular objetos do tipo string, como interpolar valores de variáveis e entender como funciona o fatiamento.

#Maiúscula, minúscula e título

curso = "pYthon"

print(curso.upper())
#>>>> PYTHON

print(curso.lower())
#>>>> python

print(curso.title())
#>>>> Python

#Para cortar os espaços

curso = "  Python "

print(curso.strip())
#>>>> "Python"

print(curso.lstrip())
#>>>> "Python "

print(curso.rstrip())
#>>>> "  Python"

#Junções e centralização

curso = "Python"

print(curso.center(10, "#")) #o número indica a quantidade de caracteres que deverá ter. o valor entre aspas, é o que irá preencher os espaços até completar a quantidade de caracteres que foi indicado. Se nao colocar nenhum caracter, ele vai preencher com espaços em brancos.
#>>>> "##Python##"

print(".".join(curso))
#>>>> "P.y.t.h.o.n"

