import random


class ChuteONumero:
    def __init__(self):
        self.tentativas = 1
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:

            if int(self.valor_do_chute) > self.valor_aleatorio:
                print('Chute um valor mais baixo!')
                self.tentativas += 1
                self.PedirValorAleatorio()

            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print('Chute um valor mais alto!')
                self.tentativas += 1
                self.PedirValorAleatorio()

            else:
                self.tentar_novamente = False
                print(
                    f'Parabéns, você acertou em {self.tentativas} tentativas!!')

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(
            self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()
