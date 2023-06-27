# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


import random
import time

numero = int(input('Descubra o numero entre 0 e 5: '))

#numeroSorteio = [0, 1, 2, 3, 4, 5]
sorteio = random.randint(0, 5)

print('PROCESSANDO...')

time.sleep(2)
if sorteio == numero:
    print('Você acertou! Parabens!!')
else:
    print('Você errou! O numero certo era {}'.format(sorteio))
