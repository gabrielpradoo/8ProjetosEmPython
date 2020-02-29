# Simulador de dado
# Simular o uso de um dado gerando um valor
import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

        # Layout
        self.layout = [
            [sg.Text(self.mensagem)],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        # Criar uma Janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com os valores
        try:
            if self.eventos == 'Sim':
                self.GerarValorDoDado()
            elif self.eventos == 'Não':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não!')
        except:
            print('Ocorreu um erro ao receber sua resposta.')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
