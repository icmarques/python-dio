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

# Interpolação de variáveis

#Em python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format e a última é utilizando f strings.
#A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo iremos focar nas 2 últimas.

nome = "Guilherme"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
idade = 28
profissao = "Programador"
linguagem = "Python"


print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(linguagem=linguagem, profissao=profissao, idade=idade, nome=nome))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa)) #dicionário

#Com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}") #o espaço antes do ponto, define quantas casas vai ter entre o item e a resposta
#>>>> "Valor de PI: 3.14"


print(f"Valor de PI: {PI:10.2f}")
#>>>> "Valor de Pi:    3.14"


