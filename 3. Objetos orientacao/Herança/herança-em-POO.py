Herança
#É a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base).

Benefícios da herança:
#Representa bem os relacionamentos do mundo real;
#Fornece reutilização de código, permitindo adicionar mais recursos a uma classe sem modificá-la;
#É a natureza transitiva, ou seja, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

Exemplo:
    #sintaxe de herança
    
    class A:
        pass
    
    class B(A): #entre parenteses é a classe que esetá sendo herdada (sendo estendida)
        pass
    
    
    
Herança simples e herança múltipla

>Herança simples: é quando uma classe filha herda apenas uma classe pai (classe base).

>Herança múltipla: é quando uma classe filha herda de várias classes pai.

Exemplo herança múltipla:
    
    class A:
        pass
    class B:
        pass
    class C (A, B):
        pass
    
