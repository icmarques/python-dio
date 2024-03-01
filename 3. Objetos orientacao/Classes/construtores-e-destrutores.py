Métodos __init__ e __del__

Método construtor (inicializador)
#O método construtor sempre é executado quando uma nova instância da classe é criada.
#Nesse método inicializamos o estado do nosso objeto.
#Para declarar o método construtor da classe, criamos um método com o nome __init__.

Exemplo:
    
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome 
        self.cor = cor 
        self.acordado = acordado
#o que vai dentro do método são os atributos e oatributos, são as características da classe

Método destrutor
#Sempre é executado quando uma instância (objeto) é destruída.
#Para declarar o método destrutor da classe, criamos um método com o nome __del__
#Mas o python já tem um coletor de lixo (que é um mecanismo interno de gerenciamento de memória)

Exemplo:
    
class Cachorro:
    def __del__(self):
        print("Destruindo a instância")
        
c = Cachorro()
del c
        