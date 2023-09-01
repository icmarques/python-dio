#Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), informando início (start), fim (stop) e passo (step): [start: stop[,step]]

nome = "Guilherme Arthur de Carvalho"

nome[0]
#>>>> "Guilherme"

nome[:9]
#>>>> "Guilherme"

nome[10:]
#>>>> "Arthur de Carvalho"

nome[10:16]
#>>>> "Arthur"

nome[10:16:2]
#>>>> "Atu"

nome[:]
#>>>> "Guilherme Arthur de Carvalho"

nome[::-1]
#>>>> "ohlavraC ed ruhtrA emrehliuG"


