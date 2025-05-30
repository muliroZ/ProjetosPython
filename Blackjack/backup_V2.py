# Feito por: muliroZ
# Github: github.com/muliroZ
# Instagram: muliro_dkl
# 
#                                                   -Blackjack-                                                                                        

import random
from time import sleep

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f'{self.valor} de {self.naipe}'
    
    def get_valor(self):
        if self.valor in ['Valete', 'Dama', 'Rei']:
            return 10
        elif self.valor == 'Ás':
            return 11
        else: return int(self.valor)

class Baralho:
    valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
    naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']

    def __init__(self):
        self.cartas = [Carta(valor, naipe) for valor in self.valores for naipe in self.naipes]
        self.embaralhar()

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self):
        return self.cartas.pop() if self.cartas else None
    
    def recolher(self, carta):
        self.cartas.extend(carta)
        self.embaralhar()
    
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def pedir_carta(self, carta):
        self.mao.append(carta)

    def val_mao(self):
        total = 0
        ases = 0

        for carta in self.mao:
            valor = carta.get_valor()
            total += valor
            if carta.valor == 'Ás':
                ases += 1

        while total > 21 and ases:
            total -= 10
            ases -= 1

        return total

    def __repr__(self):
        return f'{self.nome} está com as cartas -> {self.mao} (Total: {self.val_mao()} pontos)'
    
class Dealer:
    def __init__(self):
        self.mao = []

    def dealer_carta(self, carta):
        self.mao.append(carta)

    def pontos(self):
        total = 0
        ases = 0

        for carta in self.mao:
            valor = carta.get_valor()
            total += valor
            if carta.valor == 'Ás':
                ases += 1

        while total > 21 and ases:
            total -= 10
            ases -= 1

        return total
    
    def __repr__(self):
        return f'O dealer está com as cartas -> {self.mao} (Total: {self.pontos()} pontos)'

class Aposta:
    def __init__(self):
        pass



baralho = Baralho()
dealer = Dealer()
jogador = Jogador(input('Digite seu nome: ').strip())

# Gameplay
fim = ''

while fim == '':
    sleep(0.7)
    print('\n************* !BLACKJACK! *************\n')
    sleep(0.7)

    jogador.pedir_carta(baralho.distribuir())
    dealer.dealer_carta(baralho.distribuir())
    jogador.pedir_carta(baralho.distribuir())

    print(jogador)
    sleep(1.0)
    print(dealer)
    sleep(1.6)

    opc = str(input('Continuar (c) ou Parar (p)?: ').strip().lower())

    match opc:
        case 'c':
            jogador.pedir_carta(baralho.distribuir())
            sleep(1.0)
            print(f'\n{jogador}\n')
            if jogador.val_mao() > 21:
                sleep(1.2)
                print(f'Você perdeu!!! Total: {jogador.val_mao()} pontos\n')
            elif jogador.val_mao() == 21:
                sleep(1.2)
                print('Você atingiu a pontuação máxima!!! Total: 21 pontos\n')
            else:
                while jogador.val_mao() < 21:
                    sleep(1.0)
                    opt = str(input('Continuar (c) ou Parar (p)?: ').strip().lower())
                    if opt == 'c':
                        jogador.pedir_carta(baralho.distribuir())
                        sleep(1.2)
                        print(f'\n{jogador}')
                        if jogador.val_mao() > 21:
                            sleep(1.2)
                            print(f'Você perdeu!!! Total: {jogador.val_mao()} pontos\n')
                        elif jogador.val_mao() == 21:
                            sleep(1.2)
                            print('Você atingiu a pontuação máxima!!! Total: 21 pontos\n')
                    else:
                        dealer.dealer_carta(baralho.distribuir())
                        sleep(1.2)
                        print(f'{dealer}\n')
                        if dealer.pontos() == 21:
                            sleep(1.2)
                            print(f'O Dealer conseguiu um *Blackjack*!!! {dealer.mao}.\n')
                            break
                        else:
                            while dealer.pontos() < 17:
                                dealer.dealer_carta(baralho.distribuir())
                                sleep(1.2)
                                print(f'\nO Dealer compra uma carta!\nCartas do Dealer -> {dealer.mao}\nTotal: {dealer.pontos()} pontos\n')

                        if dealer.pontos() > 21:
                            sleep(1.2)
                            print(f'O Dealer estourou!!! Você ganhou!!! {dealer.mao} Total: {dealer.pontos()} pontos\n')
                            break
                        else:
                            sleep(1.2)
                            print(jogador)
                            sleep(1.5)
                            print(dealer, end='')
                            if jogador.val_mao() > dealer.pontos():
                                sleep(1.5)
                                print('Parabéns, você ganhou!!!\n')
                            elif jogador.val_mao() < dealer.pontos():
                                sleep(1.5)
                                print('Você perdeu, que pena!!!\n')
                            else:
                                sleep(1.5)
                                print('Houve um empate!\n')
                            break
        case 'p':
            dealer.dealer_carta(baralho.distribuir())
            sleep(1.2)
            print(f'\n{dealer}\n')
            if dealer.pontos() == 21:
                sleep(1.2)
                print(f'O Dealer conseguiu um *Blackjack*!!! {dealer.mao}.\n')
            else:
                while dealer.pontos() < 17:
                    dealer.dealer_carta(baralho.distribuir())
                    sleep(1.2)
                    print(f'\nO Dealer compra uma carta!\nCartas do Dealer -> {dealer.mao}\nTotal: {dealer.pontos()} pontos\n')

                if dealer.pontos() > 21:
                    sleep(1.2)
                    print(f'O Dealer estourou!!! Você ganhou!!! {dealer.mao} Total: {dealer.pontos()} pontos\n')
                else:
                    sleep(1.2)
                    print(jogador)
                    sleep(1.2)
                    print(dealer)
                    if jogador.val_mao() > dealer.pontos():
                        sleep(1.5)
                        print('\nParabéns, você ganhou!!!\n')
                    elif jogador.val_mao() < dealer.pontos():
                        sleep(1.5)
                        print('\nVocê perdeu, que pena!!!\n')
                    else:
                        sleep(1.5)
                        print('\nHouve um empate!\n')

    baralho.recolher(jogador.mao)
    baralho.recolher(dealer.mao)

    jogador.mao.clear()
    dealer.mao.clear()

    fim = input('Jogar outra rodada? (Aperte "Enter" para continuar):').strip()