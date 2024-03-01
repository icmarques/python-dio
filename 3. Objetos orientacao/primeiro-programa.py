#PRIMEIRO PROGRAMA
    
#João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
#Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
#Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos.
    
class Bicicleta:
#este primeiro def é o construtor
    def __init__(self, cor, modelo, ano, valor):  #self representa a instancia do proprio objeto (é o próprio objeto). Sempre colocar.
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor #self. são os atributos da classe
        
 
 #def + nome do método + (self)       
    def buzinar (self): #metodos são funções que estão dentro de uma classe. São iguais as funçoes, mas precisam do self como argumento
        print("Plim Plim")

    def parar (self):
        print("Parando bicicleta...")
        print("Bicicleta parada")
        
        
    def correr (self):
        print("Vruuuummm...")
        
    
            
b1 = Bicicleta("azul", "BMX", 2005, 500)
b2 = Bicicleta("vermelho", "caloi", 2010, 300)
    
b1.buzinar()
b1.parar()   
b1.correr()

print(b1.cor, b1.modelo, b1.ano, b1.valor) #serve para acessar os atributos. 


Bicicleta.buzinar(b2) #é equivalente a b2.buzinar()

print(b2.cor, b2.modelo, b2.ano, b2.valor)

print(b2.cor)

#def __str__(self):
        #return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
#desta maneira, é possível trazer as informaçoes dos atributos


  #def __str__(self):
    #  return f"{self.__class__.__name__}" 
#traz o nome da classe

  #def __str__(self):
    #  return f"{self.__class__.__name__}: {', '.join([f" {chave} = {valor}]}" for chave, valor in self.__dict__.items()])}"
#serve para fazer as representações de classe    
