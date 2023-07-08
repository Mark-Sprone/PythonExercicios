#  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

atual = datetime.date.today().year
maior = 0
menor = 0

for pessoa in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu: '.format(pessoa)))
    idade = atual - ano
    if idade >= 18:
        maior = maior +1
    else:
        menor = menor + 1

print('Tivemos {} pessoas maiores de idade.'.format(maior))
print('Tivemos {} pessoas menor de idade.'.format(menor))
