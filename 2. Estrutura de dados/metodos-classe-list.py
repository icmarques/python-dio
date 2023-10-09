#[].append
#Serve para adicionar outro elemento à lista.
#os elementos adicionados aparecem após os elementos da lista original

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)
#>>>> [1, "Python", [40, 30, 20]]


#[].clear
#Serve para limpar a lista

lista = [1, "Python", [40, 30, 20]]

print(lista)
#>>>> [1, "Python", [40, 30, 20]]

lista.clear()
print(lista)
#>>>> []


#[].copy
#vai retornar a lista, mas com uma instancia diferente
#as alterações feitas na lista.copy não refletem na lista original

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)



#[].count
#é utilizado para contar quantas vezes um determinado objeto aparece dentro da lista

cores = [1, 2, 3, 2]

cores.count[1] #1
cores.count[2] #2
cores.count[3] #1


#[].extend
#faz a junção de listas
#se há um mesmo elemento em mais de uma lista, ele aparece repetidamente no resultado final
#os elementos adicionados aparecem após os elementos da lista original

linguagens = ["python", "js", "c"]

print(linguagens) #["python", "js", "c"]

linguagens.extend(["java", "c"])

print(linguagens) #["python", "js", "c","java", "c" ]



#[].index
#traz a primeira ocorrência do elemento dentro da lista
#ele não traz todas as ocorrências do elemento dentra da lista

linguagens = ["python", "js", "c","java", "c" ]

print(linguagens.index("java")) #3
print(linguagens.index("pyton")) #0



#[].pop
#ele retira os elementos da lista do último para o primeiro (respeitando a pilha de elementos)
#também é possível passar a posição do elemento a ser retirado da lista, independentemente da ordema da pilha

linguagens = ["python", "js", "c","java", "csharp" ]

linguagens.pop() #csharp
linguagens.pop() #java
linguagens.pop() #c
linguagens.pop(0) #python



#[].remove
#retira elementos da lista indicando qual o elemento a ser removido ao invés do índice (posicionamento) do elemento
#ele retira apenas a primeira ocorrência do elemento

linguagens = ["python", "js", "c","java", "c" ]

linguagens.remove("c")

print(linguagens) #["python", "js","java", "c"]



#[].reverse
#inverte a ordem da lista, mudando o último elemento para a primeira posição, o penúltimo para segunda posição e assim sucessivamente

linguagens = ["python", "js", "c","java", "c" ]

linguagens.reverse()

print(linguagens) #["c", "java", "c", "js", "python"]



#[].sort
#ordena os elementos alfabeticamente, ordem crescente

linguagens = ["python", "js", "c","java", "c" ]
linguagens.sort() #["c", "c" "java", "js", "python"]

linguagens = ["python", "js", "c","java", "c" ]
linguagens.sort(reverse=True) #["python", "js", "java", "c", "c"] => com o reverse, ele irá ordenar de trás para frente (decrescente)

linguagens = ["python", "js", "c","java", "c" ]
linguagens.sort(key=lambda x: len(x)) #["c", "c", "js", "java", "python"] => lambda é uma função anônima. E com a função indicada, para cada elemento, ele irá contar a quantidade de caracteres e organizar do menor para o maior(crescente)

linguagens = ["python", "js", "c","java", "c" ]
linguagens.sort(key=lambda x: len(x), reverse=True) #["python", " "java", "js", c", "c"] => idem a função anterior, mas com o reverse, ele ordena do maior para o menor(decrescente)



#len
#mostra o tamanho dos elementos, no caso, o tamanho da lista

linguagens = ["python", "js", "c","java", "c"]

len[linguagens] #5



#sorted
#serve para ordenar a lista

linguagens = ["python", "js", "c","java", "csharp" ]

sorted(linguagens, key=lambda x: len(x)) #["c", "js", "java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) #["python", "csharp", "java", "js", "c"]