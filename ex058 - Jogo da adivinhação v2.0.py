'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
 mostrando no final quantos palpites foram necessários para vencer.'''

import random
cont = 0

sorteio = random.randint(0, 10)
numero = int(input('Digite um número entre 0 e 10: '))

while numero != sorteio:
    cont += 1
    if numero > sorteio:
        print('Menos...')
    elif numero < sorteio:
        print('Mais...')
    numero = int(input('Você errou! Digite novamente: '))
    
print('Você Acertou!! PARABÉNS!! Você tentou {}'.format(cont))


