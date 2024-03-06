class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): #**kw = keywargs, que permite usar os argumentos da classe pai
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
   def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass


gato = Gato(nro_patas=4, cor_pelo="preto")
cachorro = Cachorro(nro_patas=4, cor_pelo="caramelo")
leao = Leao(nro_patas=4, cor_pelo="amarelo")

print(gato)
print(cachorro)
print(leao)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
#como foi usado **kw, é preciso informar chave e valor, pois o posicional não irá funcionar já que dizemos "todas as chaves da classe pai + as chaves específicas da classe filho", sem ordem definida

