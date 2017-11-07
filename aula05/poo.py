class Banco:
    saldo = 0
    correntista = ""
    titular =''
    cpf = None
    idade = None

    def __init__(self, dados):
        self.titular = dados['nome']
        self.cpf = dados['cpf']
        self.idade = dados['idade']

    def consultar_titular(self):
        return self.titular

    def consultar_saldo(self):
        return self.saldo

    def deposito(self, valor):
        self.saldo += valor
        return valor

    def saque(self, valor):
        if self.checar_saldo(valor):
            self.saldo -= valor
            return 'Valor descontado'
        else:
          return 'Saldo insuficiente'
    def checar_saldo(self,valor):
        return False if self.saldo<=valor else True

class Conta(Banco):
    def __init__(self, dados):
        self.titular = dados['nome']
        self.cpf = dados['cpf']
        self.idade = dados['idade']

    def saque(self, valor):
        if self.checar_saldo(valor):
            self.saldo -= valor
            return 'Valor descontado'
        else:
            return 'Saldo insuficiente'




cadastro={'nome':'Vitor Pires','idade':'30','cpf':'123456789'}

objeto = Banco(cadastro)
objeto.deposito(1000)
print(objeto.consultar_saldo())


print(objeto.saque(500))