#São estruturas utilizadas para repetir um trecho de cõdigo um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

#exemplo sem repetição

a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

#Comando for

#É usado para percorrer um objeto iterável.
#Faz sentido usar quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end= " ")

print() #adiciona um a quebra de linha