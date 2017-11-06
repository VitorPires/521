class Carro:
    velocidade_maxima = 100
    velocidade_atual = 0

    def acelerar(self,velocidade):
        if(self.velocidade_atual + velocidade) <= self.velocidade_maxima:
           self.velocidade_atual=+velocidade
           raise Exception('Velocidade aumentada (%s)'% self.velocidade_maxima)
           #print('Velocidade aumentada (%s)'% self.velocidade_maxima)



    def frear(self,velocidade):
        if (self.velocidade_atual - velocidade)>=0:
            self.velocidade_atual-=velocidade
            raise Exception('Velocidade reduzida (%s)' % self.velocidade_atual)
        else:
            raise Exception('Nao foi possicel reduzir')


try:
 objeto = Carro()
 objeto.acelerar(210)
 objeto.frear(50)
except Exception as e:
    print(e)

