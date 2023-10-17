#Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses par6ametros podem ou nào ter valores padrões.
#Usar funções torna o código mais legível e possibilita o reaproveitamento de código.
#Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada.

def exibir_mensagem():
    print("Olá mundo!")
    
def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo {nome}")
    
def exibir_mensagem_3(nome="Anônimo")


exibir_mensagem()
exibir_mensagem_2("Carla")
exibir_mensagem_3()

#Para que a função seja executada, é preciso chamar a função.


# Retornando valores
#Para retornar um valor, utilizamos a palavra reservada return.
#Toda função python retorna None por padrão. 
#Diferente de outras linguagens de programação, em Python um afunção pode retornar mais de um valor.

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

calcular_total([10, 20, 34]) #64
retorna_antecessor_e_sucessor(10) #(9,11)


# Argumentos nomeados
#Funções também podem ser chamados usando argumentos nomeados da forma chave=valor.


# Args e Kwargs
#*args: valores vem como uma tupla
#**kwargs: valores vão vir num dicionário
#são os asteriscos que indicam se é arg ou kwarg


# Parâmetros especiais
#Por padrão, argumentos podem ser passados para uma função python tanto por posição quanto explicidamente pelo nome.
#Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passadas.
#Assim, um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome ou por nome.



# Objetos de primeira classe
#Em python tudo é objeto, dessa forma funções também são objeto o que as tornam objetos de primeira classe. 
#Com isso, pode-se atribuir funções a variaveis, passá-ldas como parâmetro para funções, usá-ldas como valores em estruturas de dados(listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures).