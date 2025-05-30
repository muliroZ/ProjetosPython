import random

class Apostador:
    def __init__(self):
        self.fichas = 1000

    def apostar(self, valor):
        if valor <= self.fichas and valor > 0:
            self.fichas -= valor
            return valor
        else: return 'Saldo insuficiente'

    def __repr__(self):
        return f'Voce tem {self.fichas} fichas.'

player = Apostador()

while True:
    while True:
        print(player)
        aposta = player.apostar(int(input('Coloque sua aposta -> ')))
        if aposta == 'Saldo insuficiente':
            break

        escolha = int(input(f'Escolha um numero de 1 a 5 -> '))

        tabela = [1, 2, 3, 4, 5]
        resultado = random.choice(tabela)
        print(f'\nNumero escolhido -> {resultado}')

        if escolha == resultado:   
            premio = int(aposta + aposta*1.5)
            player.apostar(int((aposta + premio)*-1))
            print(f'\nParabens! Voce ganhou {premio} fichas!!! Lucro: {int(aposta*1.5)}\n')
        else:
            print(f'\nQue pena! Voce perdeu {aposta} fichas!!!\n')

        print(player)

        opc = input('\nQuer apostar de novo? (y or n)\n').lower
        if opc == 'n': break
    
    opc = input(f'\n{aposta}:( - Quer apostar de novo? (y or n)\n').lower()
    if opc == 'n': break