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

# O do Jogador e o do Dealer eram iguais, eu só eliminei a redundância
def calcular_pontos(mao):
    total = 0
    ases = 0

    for carta in mao:
        valor = carta.get_valor()
        total += valor
        if carta.valor == 'Ás':
            ases += 1

    while total > 21 and ases:
        total -= 10
        ases -= 1

    return total

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.fichas = 1000
        self.mao = []

    def apostar(self, valor):
        if valor <= self.fichas and valor > 0:
            self.fichas -= valor
            return valor
        else: return False

    def pedir_carta(self, carta):
        self.mao.append(carta)

    def val_mao(self):
        return calcular_pontos(self.mao)

    def __repr__(self):
        return f'{self.nome} está com as cartas -> {self.mao} (Total: {self.val_mao()} pontos) - Fichas: {self.fichas}'
    
class Dealer:
    def __init__(self):
        self.mao = []

    def dealer_carta(self, carta):
        self.mao.append(carta)

    def pontos(self):
        return calcular_pontos(self.mao)
    
    def __repr__(self):
        return f'O dealer está com as cartas -> {self.mao} (Total: {self.pontos()} pontos)'

baralho = Baralho()
dealer = Dealer()
jogador = Jogador(input('Digite seu nome: ').strip())

# Funções aux. (se repetiam no código)
def dealer_vez():
    dealer.dealer_carta(baralho.distribuir())
    sleep(1.2)
    print(f'\n{dealer}\n')
    if dealer.pontos() == 21:
        sleep(1.2)
        print(f'O Dealer conseguiu um *Blackjack*!!! {dealer.mao}. (-{aposta} Fichas)\n')
        if aposta_seguro:
            jogador.fichas += aposta
            print(f'\nO seguro te salvou! Sem perdas essa rodada. Fichas: {jogador.fichas}')
        return False
    while dealer.pontos() < 17:
        dealer.dealer_carta(baralho.distribuir())
        sleep(1.2)
        print(f'\nO Dealer compra uma carta!\nCartas do Dealer -> {dealer.mao}\nTotal: {dealer.pontos()} pontos\n')
    if dealer.pontos() > 21:
        sleep(1.2)
        print(f'O Dealer estourou!!! {dealer.mao} Total: {dealer.pontos()} pontos\n')
        return True
    return True

def resultado_partida():
    sleep(1.2)
    print(jogador)
    sleep(1.2)
    print(dealer)
    if jogador.val_mao() > dealer.pontos() and jogador.val_mao() <= 21:
        sleep(1.5)
        print(f'\nParabéns, você ganhou!!! (+{aposta*2} Fichas)\n')
        jogador.fichas += aposta*2
    elif jogador.val_mao() < dealer.pontos() and dealer.pontos() <= 21:
        sleep(1.5)
        print(f'\nVocê perdeu, que pena!!!  (-{aposta} Fichas)\n')
    elif (jogador.val_mao() == dealer.pontos()) or (jogador.val_mao() > 21 and dealer.pontos() > 21):
        sleep(1.5)
        print('\nHouve um empate! Sem perdas!\n')
        jogador.fichas += aposta

def compra():
    jogador.pedir_carta(baralho.distribuir())
    sleep(1.2)
    print(f'\n{jogador}')
    if jogador.val_mao() > 21:
        sleep(1.2)
        print(f'Você estourou!!! Total: {jogador.val_mao()} pontos (-{aposta} Fichas)\n')
        return True
    elif jogador.val_mao() == 21:
        sleep(1.2)
        print('Você atingiu a pontuação máxima!!! Total: 21 pontos\n')
        if dealer_vez():
            resultado_partida()
        return False
    return True

# Funções principais
def stop():
    if dealer_vez():
        resultado_partida()

def cont():
    compra()
    while jogador.val_mao() < 21:
        sleep(1.0)
        opt = str(input('Continuar (c) ou Parar (p)?: ').strip().lower())
        if opt == 'c':
            compra()
        else:
            if dealer_vez():
                resultado_partida()
            break

def dobro():
    global aposta
    aposta *= 2
    print(f'\nAposta DOBRADA: {aposta//2} -> {aposta} Fichas')
    print('')
    if compra():
        if dealer_vez():
            resultado_partida()

def seguro():
    if jogador.val_mao() == 21 and dealer.pontos() == 11:
        print('Aposta de Seguro\n' \
        '1 - Receber o valor da aposta (2:1) imediatamente\n' \
        '2 - Não fazer a aposta de seguro\n')
        opt = int(input('-> '))

        if opt == 1:
            jogador.fichas += aposta*2
            print(f'Você recebeu {aposta*2} Fichas (2:1)!')
            return False

    elif jogador.val_mao() < 21 and dealer.pontos() == 11:
        print('Aposta de Seguro\n' \
        '1 - Fazer o seguro (Metade da aposta inicial) contra o blackjack\n' \
        '2 - Não fazer a aposta de seguro\n')
        opt = int(input('-> '))

        if opt == 1:
            jogador.fichas -= aposta/2
            return True

    elif jogador.val_mao() == 21 and dealer.pontos() != 11:
        print(f'Você conseguiu um BLACKJACK! (+{aposta*2 + aposta/2} Fichas)')
        jogador.fichas += aposta*2 + aposta/2
        return False
    
    else: return None

# Controla o fim da rodada/jogo
def final():
    baralho.recolher(jogador.mao)
    baralho.recolher(dealer.mao)

    jogador.mao.clear()
    dealer.mao.clear()

    fim = input().strip()
    if fim != '':
        return True

# Gameplay
while True:
    while True:
        sleep(0.7)
        print('\n************* - ! BLACKJACK ! - *************\n')
        sleep(0.7)

        print(f'Você tem {jogador.fichas} fichas.')
        aposta = jogador.apostar(int(input('Sua aposta -> ')))
        if aposta == False: break
        sleep(0.7)

        jogador.pedir_carta(baralho.distribuir())
        dealer.dealer_carta(baralho.distribuir())
        jogador.pedir_carta(baralho.distribuir())

        print('')
        print(jogador)
        sleep(1.0)
        print(dealer)
        sleep(1.5)

        if seguro():
            aposta_seguro = aposta/2
        elif seguro() == False:
            break
        else: None

        opc = str(input('Continuar (c), Parar (p) ou Dobrar (d)?: ').strip().lower())
        if opc not in ['c', 'p', 'd']: break

        match opc:
            case 'c':
                cont()
            case 'p':
                stop()
            case 'd':
                dobro()

        print('Jogar outra rodada? (Aperte "Enter" para continuar):')
        if final():
            break

    print('Me parece que você fez algo invalido! :( (Enter para reiniciar)')
    if final():
        break

# Código ainda em desenvolvimento.