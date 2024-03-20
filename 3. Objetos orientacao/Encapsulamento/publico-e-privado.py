Recursos públicos são aqueles que é possível acessar fora da classe.

Recurso privado é aquele que só se altera dentro da classe ou do método.
    Normalmente iniciado com underline.
    
    
Exemplo:
    class Conta:
    def __init__(self, saldo=0)
        self._saldo = saldo
        
    def despositar (self, valor):
        pass
    
    def sacar (self, valor):
        pass