#São estruturas utilizadas para repetir um trecho de cõdigo um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

#exemplo sem repetição

#a = int(input("Informe um número inteiro: "))
#print(a)

#a += 1
#print(a)

#a += 1
#print(a)

#Comando for

#É usado para percorrer um objeto iterável.
#Faz sentido usar quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

#texto = input("Informe um texto: ")
#VOGAIS = "AEIOU"

# for letra in texto:
   # if letra.upper() in VOGAIS:
        #print(letra, end= " ")

#print() #adiciona um a quebra de linha

# Comando for else:

#texto = input("Informe um texto: ")
#VOGAIS = "AEIOU"

#for letra in texto:
    #if letra.upper() in VOGAIS:
        #print(letra, end= " ")

#else:
    #print() #adiciona um a quebra de linha
    #print("Executa no final do laço")
    
# Função range

#Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo).
#Se usarmos range (i, j) será produzido:

    #i, i+1, i+2, i+3, ..., j-1.

#Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.

#list(range(4))
#>>>> [0, 1, 2, 3]  #range(stop) -> range object

# Utilizando range com for

#for numero in range(0,11):
#    print(numero, end=" ")
#>>>> 0 1 2 3 4 5 6 7 8 9 10

#exibindo a tabuada do 5
#for numero in range(0, 51, 5): #0 start, 5 step opcional e 51 stop
    #print(numero, end=" ")
#>>>> 0 5 10 15 20 25 30 35 40 45 50

# Comando while

#O comando while é usado para repetir um bloco de código várias vezes.
#Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))
    
    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo o extrato ...")
        
else: 
    print("Obrigado por usar nosso sistema bancário, até logo!")
    

