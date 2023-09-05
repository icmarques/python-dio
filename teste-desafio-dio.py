import sys
#a = int(sys.stdin.readline())
#print(a)

twitter = input("Escreva seu tweet aqui: " )
qtd_caracteres = len(twitter)
#print(qtd_caracteres)

variavel_1 = "TWEET"
variavel_2 = "MUTE"

if qtd_caracteres <= 140:
    print(variavel_1)
    
else:
    print(variavel_2)
    

