#PRIMEIRO PROGRAMA
    
#João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
#Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
#Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos.
    
class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):  #self representa a instancia do proprio objeto. Sempre colocar.
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar (self):
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

print(b1.cor, b1.modelo, b1.ano, b1.valor) #serve para demonstrar os atributos. 


b2.buzinar()
print(b2.cor, b2.modelo, b2.ano, b2.valor)