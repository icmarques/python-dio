class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
        
    def depositar(self, valor):
        self._saldo += valor
        
    def sacar(self, valor):
        self._saldo += valor
        
    def mostrar_saldo(self): #modo correto de acessar o que está privado, é com um método
        return self._saldo

conta = Conta("0001", 100)
#conta._saldo += 100 este é um exemplo de má prática

conta.depositar(100)
print(conta._saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo())