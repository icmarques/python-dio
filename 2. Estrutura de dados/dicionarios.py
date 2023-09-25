#É um conjunto não ordenado de pares chave: valor onde as chaves são únicas em uma dada instancia do dicionario.
#São delimitados por: {} e contém uma lista de pares chace: valor separada por vírgulas. A atribuição é feita com :
#Pode-se usar também a classe dict, onde a chave e o valor ficarão entre parenteses e atribuição é feita pelo sinal de =, dividindo as duplas por virgula

pessoa = {"nome": "Guilherme", "idade": 28} #a chave é o nome e o valor é Guilherme; chave idade e valor 28

pessoa = dict(nome="Guilherme", idade=28) #a chave é o nome e o valor é Guilherme; chave idade e valor 28

pessoa["telefone"] = "3333-3333" #{"nome": "Guilherme", "idade": 28, "telefone": "3333-3333"}


#Para acessar o argumento que está dentro do dicionário, deverá:
    #ser usada o nome do dicionário (a variável que identifica);
    #[];
    #e o nome da chave dentro dos conchetes
    
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-3333"}

dados["nome"] #Guilherme
dados["idade"] #28
dados["telefone"] #3333-3333

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "1111-1111"

#dados = "nome": "Maria", "idade": 18, "telefone": "1111-1111"



# Dicionários aninhados
#Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde uqe a chave para esse valor seja um objeto imutável como strings e números.

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-3333"}
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
    
}

contatos["guilherme@gmail.com"]["telefone"] # "3443-2121"

