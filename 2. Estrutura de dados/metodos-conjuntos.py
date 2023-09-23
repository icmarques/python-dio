# Métodos da classe do set(conjuntos)

#{}.union
#Une os dois conjuntos

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) #{1, 2, 3, 4}


#{}.intersection
#traz somente os elementos que constam em ambos os conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) #{2, 3}


#{}.difference
#traz o elemento que existe somente no conjunto comparado

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) #{1}
conjunto_a.difference(conjunto_a) #{4}


#{}.symetric_difference
#traz todos os elementos que nâo estão na intersecção

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) #{1, 4}


#{}.issubset
#traz se um conjunto pertence a outro conjunto

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1 , 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) #True
conjunto_b.issubset(conjunto_a) #False

#{}.issuperset
#indica quando um conjunto não pertence a outro

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1 , 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) #False
conjunto_b.issubset(conjunto_a) #True


#{}.isdisjoint
#indica quando todo o conjunto não consta em outro conjunto

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) #True
conjunto_a.isdisjoint(conjunto_c) #False


#{}.add
#adiciona elementos que não existem no conjunto
#se o elemento já existe, ele não adiciona mais um elemento igual ao conjunto

sorteio = {1, 23}

sorteio.add(25) #{1, 23, 25}
sorteio.add(42) #{1, 23, 25, 42}
sorteio.add(25) #{1, 23, 25, 42}


#{}.clear
#limpa (exclui) os elementos de um conjunto

sorteio = {1, 23}

sorteio #{1, 23}
sorteio.clear()
sorteio # {}


#{}.copy
#copia os elementos de um conjunto

sorteio = {1, 23}

sorteio #{1, 23}
sorteio.copy()
sorteio #{1, 23}


#{}.discard
#descarta um valor existente dentro do conjunto
#se informado um valor que não existe, ele não informa erro e também não altera em nada o conjunto

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros #{1, 2, 3, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
numeros #{2, 3, 4, 5, 6, 7, 8, 9, 0}


#{}.pop
#remove o valor da lista em ordem (da esquerda para a direita), sem precisar informar o argumento

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop() #0
numeros.pop() #1
numeros #{2, 3, 4, 5, 6, 7, 8, 9}


#{}.remove
#descarta um valor existente dentro do conjunto
#se informado um valor que não existe, ele vai informa erro e não altera em nada o conjunto 

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.remove(0)
numeros #{1, 2, 3, 4, 5, 6, 7, 8, 9}


#len
#serve para verificar o tamanho do conjunto
#ele não conta elementos duplicados

numeros = {1, 2, 3, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 0}
len(numeros) #10


in
#retorna se o elemento indicado consta dentro de um conjunto

numeros = {1, 2, 3, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros #True
10 in numeros #False