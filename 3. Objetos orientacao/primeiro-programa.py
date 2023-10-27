#PRIMEIRO PROGRAMA
    
    #João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
    #Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
    #Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos.
    
class _init_(self, cor, modelo, ano, valor, correr=True):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
        
    def buzinar (self):
        print("Bi bi bi")
            
    def parar (self):
        self.correr=False
        print("Bicicleta parada")
            
bicicleta_1 = Bicicleta("azul", "BMX", 2005, "R$500,00", True)
bicicleta_2 = Bicicleta("vermelha", "Caloi", 2010, "R$250,00", False)
bicicleta_3 = Bicicleta("branca", "Monark", 2009, "R$1.500,00", True)
    
bicicleta_3.buzinar()
print(bicicleta_3.buzinar)
    
bicicleta_2.parar()
print(bicicleta_2.parar)
    
bicicleta_1.correr()
print(bicicleta_1.correr)

