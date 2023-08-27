#Indentar código:

#é uma forma de manter o código fonte mais legível e manutenível. 
#Mas em Python ela exerce um segundo papel através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

#Bloco de comando:
#As linguagens de programação costuman utilizar caracteres ou palavras reservadas para terminar o início e o fim do bloco
#Em Java e C, por eemplo, utilizamos chaves:

#Em Python:

#Existe uma convenção que define as boas práticas para scrita de código na linguagem.
#Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

def sacar(self, valor: float) flechinha None: # início do bloco do método
    
    if self.saldo >= valor: # início do bloco do if
        
        self.saldo -= valor
        
    # fim do bloco if
        
#fim do bloco do método