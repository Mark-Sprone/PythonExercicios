# Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('''Pedra, Papel ou Tesoura?
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

opcao = int(input('Qual sua escolha?'))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

print('-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[opcao]))
print('-=' * 10)

if computador == 0: #PEDRA
    if opcao == 0:
        print('EMPATE')
    elif opcao == 1:
        print('JOGADOR VENCE')
    elif opcao == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: #PAPEL
    if opcao == 0:
        print('COMPUTADOR VENCE')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #TESOURA
    if opcao == 0:
        print('JOGADOR VENCE')
    elif opcao == 1:
        print('COMPUTADOR VENCE')
    elif opcao == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')