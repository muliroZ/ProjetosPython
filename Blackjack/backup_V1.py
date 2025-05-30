# Feito por: muliroZ
# Github: github.com/muliroZ
# Instagram: muliro_dkl
# 
#                                                   -Blackjack-                                                                                        

import random

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
        return f'{self.nome} está com as cartas: {self.mao} (Total: {self.val_mao()} pontos)'
    
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
        return f'O dealer está com as cartas: {self.mao} (Total: {self.pontos()} pontos)'
    
baralho = Baralho()
dealer = Dealer()
jogador = Jogador(input('Digite seu nome: ').strip())

# Gameplay
fim = ''

while fim == '':
    print('\n************* !BLACKJACK! *************\n')

    jogador.pedir_carta(baralho.distribuir())
    dealer.dealer_carta(baralho.distribuir())
    jogador.pedir_carta(baralho.distribuir())

    print(jogador)
    print(dealer)

    opc = str(input('Continuar (c) ou Parar (p)?: ').strip().lower())

    match opc:
        case 'c':
            jogador.pedir_carta(baralho.distribuir())
            print(f'{jogador}\n')
            if jogador.val_mao() > 21:
                print(f'Você perdeu!!! Total: {jogador.val_mao()} pontos')
            elif jogador.val_mao() == 21:
                print('Você atingiu a pontuação máxima!!! Total: 21 pontos')
            else:
                while jogador.val_mao() < 21:
                    opt = str(input('Continuar (c) ou Parar (p)?: ').strip().lower())
                    if opt == 'c':
                        jogador.pedir_carta(baralho.distribuir())
                        print(jogador)
                        if jogador.val_mao() > 21:
                            print(f'Você perdeu!!! Total: {jogador.val_mao()} pontos')
                        elif jogador.val_mao() == 21:
                            print('Você atingiu a pontuação máxima!!! Total: 21 pontos')
                    else:
                        dealer.dealer_carta(baralho.distribuir())
                        print(f'{dealer}')
                        if dealer.pontos() == 21:
                            print(f'O Dealer conseguiu um *Blackjack*!!! {dealer.mao}.')
                            break
                        else:
                            while dealer.pontos() < 17:
                                dealer.dealer_carta(baralho.distribuir())
                                print(f'\nO Dealer compra uma carta!\nCartas do Dealer: {dealer.mao}\nTotal: {dealer.pontos()} pontos\n')

                        if dealer.pontos() > 21:
                            print(f'O Dealer estourou!!! Você ganhou!!! {dealer.mao} Total: {dealer.pontos()} pontos')
                            break
                        else:
                            print(jogador)
                            print(dealer)
                            if jogador.val_mao() > dealer.pontos():
                                print('Parabéns, você ganhou!!!')
                            elif jogador.val_mao() < dealer.pontos():
                                print('Você perdeu, que pena!!!')
                            else:
                                print('Houve um empate!')
                            break
        case 'p':
            dealer.dealer_carta(baralho.distribuir())
            print(f'{dealer}\n')
            if dealer.pontos() == 21:
                print(f'O Dealer conseguiu um *Blackjack*!!! {dealer.mao}.')
            else:
                while dealer.pontos() < 17:
                    dealer.dealer_carta(baralho.distribuir())
                    print(f'\nO Dealer compra uma carta!\nCartas do Dealer: {dealer.mao}\nTotal: {dealer.pontos()} pontos\n')

                if dealer.pontos() > 21:
                    print(f'O Dealer estourou!!! Você ganhou!!! {dealer.mao} Total: {dealer.pontos()} pontos')
                else:
                    print(jogador)
                    print(dealer)
                    if jogador.val_mao() > dealer.pontos():
                        print('Parabéns, você ganhou!!!')
                    elif jogador.val_mao() < dealer.pontos():
                        print('Você perdeu, que pena!!!')
                    else:
                        print('Houve um empate!')

    baralho.recolher(jogador.mao)
    baralho.recolher(dealer.mao)

    jogador.mao.clear()
    dealer.mao.clear()

    fim = input('Jogar outra rodada? (Aperte "Enter" para continuar): ').strip()