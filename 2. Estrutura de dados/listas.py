#Podemos criar listas utilizand o construtor list, a função range ou colocando valores separados por vírgula dentro dos colchetes

#Exemplo:
frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["ferrari", "f8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

# Acesso direto
#A lista é uma sequencia, portanto podemos acessar seus dados utilizando índices
#Contamos o índice de determinada sequencia a partir de zero.

frutas = ["maçã", "laranja", "uva", "pera"]
frutas[0] #maçã
frutas[2] #uva

#Sequencias suportam indexação negativa. A contagem começa em -1.

frutas = ["maçã", "laranja", "uva", "pera"]
frutas[-1] #pera
frutas[-3] #laranja

# Listas aninhadas
#Listas podem armazenar todos os tipos de objetos Python, portanto pode-se ter listas que armazenam outras listas.
#Com isso, pode-se criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

matriz = [
    [1, "a", 2]
    ["b", 3, 4]
    [6, 5, "c"]
]

matriz[0] #[1, "a", 2]
matriz[0][0] #1
matriz[0][-1] #2
matriz[-1][-1] #"c"

#neste exemplo, o primeiro colchetes representa a linha e o segundo conchete, o posicionamento do elemento dentro da linha

# Fatiamento
#Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequencia.
#Para isso, basta passar o índice inicial e/ou final para acessar o conjunto.
#Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] #["t", "h", "o", "n"]
lista[:2] #["p", "y"]
lista[1:3] #["y", "t"]
lista[0:3:2] #["p", "t"] (inicio, fim, step) ele foi de dois em dois e por isso o 2 é o t
lista[::] #["p", "y", "t", "h", "o", "n"]
lista[::-1] #["n", "o", "h", "t", "y", "p"]

# Iterar listas
#A forma mais comum para percorrer os dados de uma lista é utilizando o comendo for.

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
    
    
# Função enumerate
#Às vezes é necessário saber qual o índice do objeto dentro do laço for. 
#Para isso podemos usar a função enumerate.

carros = ["gol", "celta", "palio"]

for indice,carro in enumerate(carros):
    print(f"{indice}: {carro}")
    
# Compreensão de listas
#A compreensão de lista oferece uma sintaxe mais curta quando você deseja: 
#criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista já existente.\
 
 
#filtro versão 1
   
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    
        
#filtro versão 2

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]


#Modificando valores versão 1

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

