class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def falar(self):
        print("Auau")
        
c = Cachorro ("Chappie", "amarelo")
c.falar()