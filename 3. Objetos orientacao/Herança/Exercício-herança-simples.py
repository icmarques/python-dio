class Veículo:
    def __init__(self, cor, placa, numero_rodas): #características em comum
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veículo): #precisa dos artigos que constam na classe pai
    pass


# class Carro(Veículo):
#     pass



# class Caminhão(Veículo):
#     def __init__(self, cor, placa, numero_rodas, carregado):
#         self.carregado = carregado
#         super().__init__(cor, placa, numero_rodas) #super()permite invovar um metodo da classe pai a qualquer momento
        
#     def esta_carregado(self): #mesmo que ela herde atributos do pai, é possível criar atributos específicos separadamente
#         print(f"{'Sim,' if self.carregado else 'Não'} estou carregado.")
        
#     def __str__(self):
#         #return self.cor
#        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"

moto = Motocicleta("preta", "abc-1234", 2) #precisa dos artigos que constam na classe pai
# carro = Carro("branco", "xde-0098", 4)
# caminhao = Caminhão ("roxo", "gfd-8712", 8, True)

print(moto)
# print(carro)
# print(caminhao)


ver o pq nao funcionou a parte da herança na moto e no carro.

