import random
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.tentativas = 1
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        sg.change_look_and_feel = 'DarkBlue9'
        # Layout
        layout = [
            [sg.Text('Seu Chute', size=(39, 0))],
            [sg.Input(size=(18, 0), key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(39, 10))]
        ]
        # criar uma janela
        self.janela = sg.Window('Chute o Número', layout=layout)
        self.GerarNumeroAleatorio()
        # self.PedirValorAleatorio()
        try:
            while True:
                # receber valores
                self.evento, self.valores = self.janela.Read()
                # Fazer algo com estes valores
                if self.evento == 'Chutar':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            self.tentativas += 1
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            self.tentativas += 1
                            break
                        else:
                            self.tentar_novamente = False
                            print(
                                f'Parabéns, você acertou em {self.tentativas} tentativas!!')
        except:
            print('Favor digitar apenas números!')

    def LerValoresDaTela(self):
        self.evento, self.valores = self.janela.Read()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(
            self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()
